# -*-coding: utf-8 -*-
#@Author: 'ljd'
#@Time：2016/9/8 15:34
import requests
import json
import os

video_path="E:\\video"
login_url="http://service.rgbvr.com/showms/rest/sysUser/login"
login_data = {
"loginName":"admin",
"password":"FfwgIp12LrHyHSvcZ5ONEi6AH2taUqFMAMsJuRsEILpQ1vol12DZuDt188xdky0i4RZ+yhE+TP7p4nBrhGY/vBDUnsrJcDSOjsFO9ITZ1sqIz5aPb9O5oUKF2vJgMW3N0NivB6a8ctD7cMYAlOy4hlxWyW/wzYs0DoaQy/WkCJs="
}
headers = {'Content-Type':'application/json'}

url="http://service.rgbvr.com/showms/rest/user/getAllReviews"


req_login= requests.post(login_url,data=json.dumps(login_data),headers=headers)

postdata=req_login.json()['data']


r = requests.post(url,data=json.dumps(postdata),headers=headers)

for i in r.json()['data']:
    video_url = i['url']
    print video_url