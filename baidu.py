# 百度翻译 http://api.fanyi.baidu.com/api/trans/product/apidoc#languageList
#/usr/bin/env python
#coding=utf8

import random
import requests
import hashlib
from fake_useragent import UserAgent
ua = UserAgent()
headers={"User-Agent": ua.random}

def translateEnglish(q):
    appid = '20190315000277522' #你的appid
    secretKey = 'b5YuifI3uySZMNos2cLH' #你的密钥
    myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt)+secretKey
    sign = hashlib.md5(sign.encode(encoding='UTF-8')).hexdigest()
    myurl = myurl+'?appid='+str(appid)+'&q='+q+'&from=zh&to=en&salt='+str(salt)+'&sign='+sign
    response = requests.get(url=myurl, headers=headers).json()
    return response['trans_result'][0]
