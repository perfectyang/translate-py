# 百度翻译 http://api.fanyi.baidu.com/api/trans/product/apidoc#languageList 要钱的，不能用了
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
    response = requests.get(url=myurl, headers=headers)
    response = requests.get(url='http://translate.google.cn/translate_a/single?client=gtx&dt=t&dj=1&ie=UTF-8&sl=auto&tl=zh_TW&q='.format(q), headers=headers)
    print('responseresponseresponse', response)
    en = '翻译出错'
    if response.status_code == 200:
        result = response.json()
        print('result', result)
        # ['trans_result']
        # print('result', result)
        # en = result[0]['dst']
    return en
