# -*-coding: utf-8 -*-
#@Author: 'ljd'
#@Time：2016/9/7 12:02

import  time
def follow(file):
    file.seek(0,2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

if __name__ == '__main__':
    logfile = open('access.log','r')
    loglines = follow(logfile)
    for line in loglines:
        print line