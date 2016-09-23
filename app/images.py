#*-* coding:utf-8 *-*
__author__ = 'ljd'
# 抓取upsplash图片
from db import db
import re
import urllib2
from bs4 import  BeautifulSoup
from models import Image_Url
lists = []

def save_images():
    headers ={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6)Gecko/20091201 Firefox/3.5.6'}
    req = urllib2.Request(url="https://unsplash.com/",headers=headers)
    content = urllib2.urlopen(req).read()

    soup = BeautifulSoup(content,'html.parser')

    # print soup.prettify()
    #获取头像
    # for link in soup.find_all("img"):
    #     print (link.get("src"))

    # 正则匹配url
    p = re.compile(r'([a-zA-z]+://[^\s]*)(\")')

    for link in soup.find_all("a"):
        for key,values in link.attrs.items():
            # if key == "background-image":
            #     print values
            if key == "style":
                val = values.split(';')[1]
                m = p.search(val)
                if m:
                    # lists.append(m.group(1))
                    # print m.group(1)
                    list_url = Image_Url(image_url=m.group(1))
                    # print list_url
                    db.session.add(list_url)
                    db.session.commit()
                    # print list_url

# return lists
# db.session.add_all(lists)
# db.session.commit()