# -*-coding: utf-8 -*-
#@Author: 'ljd'
#@Time：2016/8/30 19:41
from bs4 import BeautifulSoup
import urllib2
import re

url = 'http://ivi.bupt.edu.cn'
req = urllib2.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.75 Safari/537.36')

try:
    resp = urllib2.urlopen(req)
    data = resp.read().decode('utf-8')
    soup = BeautifulSoup(data,"html.parser")

    # print soup.prettify()
    # for i in soup.find_all('p'):
    #     if i.string is not None:
    #         print i.string
    list_urls = soup.find_all('a',href=re.compile(r'.*'))
    print len(list_urls)
    for i in list_urls:
        if re.search(r'/player',i['href']):
            print 'Pc url:' + url + i['href']
        # else:
            # print 'Mobile url:' + url + i['href']
except urllib2.HTTPError,e:
    e.code

