# 有道翻译
from fake_useragent import UserAgent
import requests
# ua = UserAgent()
# print('uaua', ua)
# agent = ua.random
headers={"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
# print('agent', agent)
def translateEnglish(text):
    url = 'http://fanyi.youdao.com/openapi.do?keyfrom=node-fanyi&key=110811608&type=data&doctype=json&version=1.1&q={}'.format(text)
    response = requests.get(url=url, headers=headers)
    en = '翻译出错'
    if response.status_code == 200:
        res = response.json()
        en = res['translation'][0].replace('"', "'")
    return en
