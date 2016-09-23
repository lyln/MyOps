# -*-coding: utf-8 -*-
#@Author: 'ljd'
#@Time：2016/8/24 15:45
#一个简单的web 接口服务，请求以json post形式

from flask import Flask,Response
app = Flask(__name__)

@app.route('/',methods=['POST'])
def hello_world():
    # f= open("C:\Users\ljd\Desktop\unity.json")
    f = open("C:\Users\ljd\Desktop\unity.json")
    iter_f = iter(f)
    data = []
    for i in iter_f:
        data.extend(i)
    # data = f.readlines()
    f.close()
    esp = Response(response=data,
    status=200,
    mimetype="application/json")
    return  esp

if __name__ == '__main__':
    app.run(host='192.168.1.189',port=5000, debug=True)