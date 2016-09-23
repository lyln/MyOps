# -*-coding: utf-8 -*-
#@Author: 'ljd'
#@Time：2016/9/23 10:40

import time
import socket
import urllib2

from bs4 import BeautifulSoup

num=1
fs=''
socket.setdefaulttimeout(10) #设置超时时间
res=urllib2.urlopen('http://www.tjhb.gov.cn/root16/mechanism/development_mana/201609/t20160921_23390.html')
htmlBytes=res.read()
soup=BeautifulSoup(htmlBytes, "html.parser")
trs=soup.find('table',{"class":"MsoNormalTable"})


print trs
# print trs.td
# fs=fs+str(trs)
res.close()



# f=file('test.txt','w') #这个例子没有写新建文件的语句，需要自己提前在相应目录建好空文件，才能通过
# f.write(fs)
#
# f.close()

#import urllib.request
#from bs4 import BeautifulSoup


#res=urllib.request.urlopen('http://www.baidu.com')
#htmlBytes=res.read()
#soup=BeautifulSoup(htmlBytes, "html.parser")


#print(soup.prettify())
