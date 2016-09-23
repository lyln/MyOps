# -*-coding: utf-8 -*-
#@Author: 'ljd'
#@Time：2016/9/18 16:15

import time
import socket
import urllib2

from bs4 import BeautifulSoup

num=1
fs=''
socket.setdefaulttimeout(10) #设置超时时间
while (num <= 2): #设置翻页数
    res=urllib2.urlopen('http://media.chinasafety.gov.cn:8090/zhengfu3/aqxkzcx_jg.jsp?currentPage='+str(num))
    htmlBytes=res.read()
    soup=BeautifulSoup(htmlBytes, "html.parser")
    trs=soup.find("table", style="border-left: 1px solid #C1DAD7;") #根据表格的style来定位表格，也可以通过id和第几个来定位，请参考函数重载
    fs=fs+str(trs)
    res.close()
    num=num+1
    time.sleep(1.5) #等待1.5s后再操作下一页

f=file('test.txt','w') #这个例子没有写新建文件的语句，需要自己提前在相应目录建好空文件，才能通过
f.write(fs)

f.close()

#import urllib.request
#from bs4 import BeautifulSoup


#res=urllib.request.urlopen('http://www.baidu.com')
#htmlBytes=res.read()
#soup=BeautifulSoup(htmlBytes, "html.parser")


#print(soup.prettify())
