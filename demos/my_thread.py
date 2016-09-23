# -*-coding: utf-8 -*-
#@Author: 'ljd'
#@Time：2016/8/24 19:49

import os
import requests
import json
import urllib2
from threading import Thread

video_path="F:\\codes\\pycode\\upload"
headers = {'Content-Type':'application/json'}
data = {}
url="http://service.rgbvr.com/showms/rest/user/getAllReviews"
video_url="http://gs.vod.rgbvr.com/rgbvr/E8jDVzB6_1472285207.flv"

r = requests.post(url,data=json.dumps(data),headers=headers)

# class AexlDown(Thread,urllib.FancyURLopener):
#     def __init__(self,threadname,url,filename,ranges=0):
#         Thread.__init__(self,name=threadname)
#         urllib.FancyURLopener.__init__(self,proxies)
#         self.name = threadname
#         self.url = url
#         self.filename = filename
#         self.ranges = ranges
#         self.downloaded = 0

try:
    f = urllib2.urlopen(video_url)
    print help(f)
except urllib2.URLError,e:
    print e.code
# data = f.read()

