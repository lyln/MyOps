# -*-coding: utf-8 -*-
#@Author: 'ljd'
#@Time：2016/9/9 11:29
import urllib2
import requests
import json
import os
import subprocess
import  logging
video_path="E:\\video"
headers = {'Content-Type':'application/json'}

url="url"
login_url="login"

# 登陆验证
login_data = {
"loginName":"admin",
"password":"passwd"
}
req_login= requests.post(login_url,data=json.dumps(login_data),headers=headers)
postdata=req_login.json()['data']

r = requests.post(url,data=json.dumps(postdata),headers=headers)

res_data = r.json()['data']

logging.basicConfig(filename='wget_download.log',level=logging.DEBUG)

def wget_download(video_url):
    cmd = 'wget %s' %video_url
    # print cmd
    status = subprocess.call(cmd,shell=True)
    if status !=0:
        logging.error('%s' + 'download is failed' + ', erro code is ' + '%s'% video_url,status)
    else:
        logging.info('%s' + 'download is success' + ', erro code is ' + '%s'% video_url,status)

for i in res_data:
    # print i['url']
    video_url = i['url']
    video_name =video_url.split('/')[-1]
    save_path = os.path.join(video_path,video_name)
    if os.path.exists(save_path):
        logging.info('%s' %video_name +'file is always down' )
        continue
    wget_download(video_url)
