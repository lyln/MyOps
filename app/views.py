#-*- coding:utf-8 -*-
__author__ = 'ljd'

from flask import render_template,flash,redirect,request,jsonify,Flask,url_for,send_from_directory
from app import app
from forms import LoginForm
from images import save_images
from models import Image_Url,Project_List,Test_user
import  random
import  json
import config
import math
from subprocess import call
import logging
import time

from flask_paginate import Pagination
from flask import Blueprint


import  os
from  werkzeug import secure_filename


@app.route('/')
def ha():
    return "haha"
@app.route('/index')
def index():
    user = {'nickname':'Walker'}
    posts = [
        {
            'author':{'nickname':'John'},
            'body':'Beautiful day in Portland'
        },
        {
            'author':{'nickname':"Susan"},
            'body':'it is so cool!'
        }

    ]
    return render_template("index.html", title = "Home",user = user,posts = posts)


@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return  redirect('/index')
    return  render_template('login.html',title='Sign IN',form = form,providers = app.config['OPENID_PROVIDERS'])

# 保存图片接口
@app.route('/save_image_url')
def save_image_url():
    status = save_images()
    return 'ok'
    # image_urls = get_images()
    # slice = random.sample(image_urls,1)
    # return ''.join(str(e) for e in slice)
    # return json.dump(slice)

# 获取图片url接口

def obj2dict(obj):
    """
    summary:
        将object转换成dict类型
    """
    memberlist = [m for m in dir(obj)]
    _dict = {}
    for m in memberlist:
        if m[0] != "_" and not callable(m):
            _dict[m] = getattr(obj,m)

    return _dict

@app.route('/get_image_url',methods=['GET'])
def get_image_url():
    page = request.args.get('page','1')  # 获取页码
    if page == 'None':
        page = '1'
    pagination = Image_Url.query.paginate(int(page), config.PER_PAGE, error_out=True)
    images = pagination.items

    total=pagination.total #数据总条数
    total=total/config.PER_PAGE   #页数的定义
    total=int(math.ceil(total))#取整进一
    return render_template('images.html',images = images, pagination = pagination ,total = total)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in config.ALLOWED_EXTENSIONS

@app.route('/upload_file',methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)



@app.route('/consolelog')
def web_console_log():
    f = open('F:\\codes\\pycode\\microblog\\app\\output.log')
    iter_f = iter(f)
    # f.close()
    return render_template('weblogs.html',txtlog=iter_f)

@app.route('/project_list')
def project_list():
    project_list = Project_List.query.all()

    return render_template('project_list.html',project_list=project_list)



# 读取文件
def follow(file):
    file.seek(0,2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

@app.route('/deploy_online')
def deploy_online():
    logging.basicConfig(filename='deploy1.log',level=logging.DEBUG)
    logging.info(call('echo hello'))

    logfile = open('deploy.log','r')
    loglines = follow(logfile)
    print(type(loglines))
    # for line in loglines:
    #     print line
    return loglines