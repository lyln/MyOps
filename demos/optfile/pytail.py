# -*-coding: utf-8 -*-
#@Author: 'ljd'
#@Time：2016/9/7 11:47

import  subprocess
logfile = 'access.log'
command = 'tail -f' + logfile
popen = subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
while True:
    line = popen.stdout.readline().strip()
    print line

