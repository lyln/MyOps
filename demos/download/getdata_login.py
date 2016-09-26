# -*-coding: utf-8 -*-
#@Author: 'ljd'
#@Time：2016/9/8 15:34
import requests
import json
import os

video_path="E:\\video"
login_url="url"
login_data = {
"loginName":"admin",
"password":"passwd"
}
headers = {'Content-Type':'application/json'}

url="list"


req_login= requests.post(login_url,data=json.dumps(login_data),headers=headers)

postdata=req_login.json()['data']


r = requests.post(url,data=json.dumps(postdata),headers=headers)

for i in r.json()['data']:
    video_url = i['url']
    print video_url
