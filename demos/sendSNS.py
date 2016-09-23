# -*-coding: utf-8 -*-
# Author: 'ljd'
# Time：2016/9/6 10:32
# Desc: 短信http接口的python代码调用示例
# https://www.yunpian.com/api/demo.html
# https访问，需要安装  openssl-devel库。apt-get install openssl-devel

import httplib
import urllib
import sys
import logging

#服务地址
sms_host = "sms.yunpian.com"
#端口号
port = 443
#版本号
version = "v1"
#智能匹配模板短信接口的URI
sms_send_uri = "/" + version + "/sms/send.json"
#模板短信接口的URI
sms_tpl_send_uri = "/" + version + "/sms/tpl_send.json"

def send_sms(apikey, text, mobile):
    """
    通用接口发短信
    """
    params = urllib.urlencode({'apikey': apikey, 'text': text, 'mobile':mobile})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPSConnection(sms_host, port=port, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str

if __name__ == '__main__':
    #修改为您的apikey.可在官网（http://www.yuanpian.com)登录后获取
    apikey = "17fd3553725929c8e7589991693612bb"
    #修改为您要发送的手机号码，多个号码用逗号隔开
    mobile = sys.argv[1]
    #修改为您要发送的短信内容
    text = "【小花秀】监控：" + sys.argv[2]

    logging.basicConfig(filename='sendSNS.log',level=logging.DEBUG)
    logging.info(text)
    logging.info(send_sms(apikey,text,mobile))
