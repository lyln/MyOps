# -*-coding: utf-8 -*-
#@Author: 'ljd'
#@Time：2016/8/24 19:49
#download下载视频脚本

import urllib2
import requests
import json
import os

video_path="E:\\video"
headers = {'Content-Type':'application/json'}

url="list"
login_url="login"

# 登陆验证
login_data = {
"loginName":"admin",
"password":"passwd"
}
req_login= requests.post(login_url,data=json.dumps(login_data),headers=headers)
postdata=req_login.json()['data']
print postdata

r = requests.post(url,data=json.dumps(postdata),headers=headers)

def download(video_url):
    try:
        f = urllib2.urlopen(video_url)
        data = f.read()
        video_name =video_url.split('/')[-1]
        save_path = os.path.join(video_path,video_name)
        with open(save_path,'wb') as code:
            code.write(data)
    except urllib2.URLError,e:
        print e.code


for i in r.json()['data']:
    video_url = i['url']
    print video_url
    video_name =video_url.split('/')[-1]
    save_path = os.path.join(video_path,video_name)
    if os.path.exists(save_path):
        print "%s file is always down" %video_name
        continue
    download(video_url)
