# -*-coding: utf-8 -*-
#@Author: 'ljd'
#@Time：2016/8/24 15:28

# list.append() 与 list.extend() 区别

list1 = [1,2,3]
list1.append(['a','b'])
print list1
print len(list1)  #len 大小是4

list2 = [1,2,3]
list2.extend(['a','b'])
print list2
print len(list2) #len 大小为5