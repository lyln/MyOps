# -*-coding: utf-8 -*-
#@Author: 'ljd'
#@Time：2016/8/31 10:31
from bs4 import BeautifulSoup
import urllib2
import os

url = 'http://tv.cctv.com/epg/'
video_path="F:\\codes\\pycode\\cctv"
req = urllib2.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.75 Safari/537.36')


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

try:
    resp = urllib2.urlopen(req)
    data = resp.read()
    soup = BeautifulSoup(data,"html.parser")
    divdata = soup.find('div',{'class':'channel_box'})
    # print divdata.ul
    for i in divdata.ul.find_all('img'):
        download(i['src'])




except urllib2.HTTPError,e:
    e.code
