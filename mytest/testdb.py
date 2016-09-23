#-*- coding:utf-8 -*-
from app.db import db

__author__ = 'ljd'

from  model import test_db
from app.models import Image_Url,Project_List
import random
import json


test_db1 = test_db(id=9,name='dasf')

# add
# db.session.add(test_db1)
# db.session.commit()

# select
select = test_db.query.filter_by(id='9').first()
print select.name

#update
# news=test_db.query.all()
# print news
# news[1].name='admin'
# db.session.commit()


#delete
# xame = test_db.query.filter_by(name = 'admin').first()
# db.session.delete(xame)
# db.session.commit()


# images = Image_url.query.count()
# print type(images)
# print images

# images = Image_url.query.paginate(1, 5, False)
# i
# print help(images)
# print dir(images)
# print type(images)
# print images.iter_pages
# for i in images.iter_pages(left_edge=2,left_current=1,right_current=3,right_edge=2):
#     print i
# print images.items
# slice = random.sample(images,1)
# print type(images)
# slice = random.sample(images,1)
# print slice[0].image_url

# def obj2dict(obj):
#     """
#     summary:
#         将object转换成dict类型
#     """
#     memberlist = [m for m in dir(obj)]
#     _dict = {}
#     for m in memberlist:
#         if m[0] != "_" and not callable(m):
#             _dict[m] = getattr(obj,m)
#
#     return _dict
#
# for i in images:
#     print json.load(str(obj2dict(i)))
# for item in images:
#     print type(item)
#     print item.image_id


project_list = Project_List.query.all()
print type(project_list)

