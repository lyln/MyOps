# -*-coding: utf-8 -*-
#@Author: 'ljd'
#@Time：2016/9/2 12:00


def foo(*args,**kwargs):
    print 'args = ', args
    print 'kwargs =', kwargs
    print '------------'

if __name__ == '__main__':
    foo(1,2,3,4)
    foo(a=1,b=2,c=3)
    foo(1,2,3,4, a=1,b=2,c=3)
    foo('a',1,None,a=1,b=2,c=3)


# *args是任意多个无名参数,它是一个tuple
# *kargs 是任意多个无名参数，它是一个dict