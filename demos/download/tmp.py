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

url="http://service.rgbvr.com/showms/rest/user/getAllReviews"
login_url="http://service.rgbvr.com/showms/rest/sysUser/login"

# 登陆验证
login_data = {
"loginName":"admin",
"password":"FfwgIp12LrHyHSvcZ5ONEi6AH2taUqFMAMsJuRsEILpQ1vol12DZuDt188xdky0i4RZ+yhE+TP7p4nBrhGY/vBDUnsrJcDSOjsFO9ITZ1sqIz5aPb9O5oUKF2vJgMW3N0NivB6a8ctD7cMYAlOy4hlxWyW/wzYs0DoaQy/WkCJs="
}
req_login= requests.post(login_url,data=json.dumps(login_data),headers=headers)
postdata=req_login.json()['data']

r = requests.post(url,data=json.dumps(postdata),headers=headers)

res_data = r.json()['data']

logging.basicConfig(filename='wget_download.log',level=logging.DEBUG)

def wget_download(video_url,video_name):
    cmd = 'wget %(url)s -OutFile %(name)s' %({'url':video_url, 'name':video_name})
    print cmd
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
    wget_download(video_url,video_name)
