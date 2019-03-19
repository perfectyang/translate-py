# 有道翻译
from fake_useragent import UserAgent
import requests
ua = UserAgent()
headers={"User-Agent": ua.random}

def translateEn(text):
    url = 'http://fanyi.youdao.com/openapi.do?keyfrom=node-fanyi&key=110811608&type=data&doctype=json&version=1.1&q={}'.format(text)
    response = requests.get(url=url, headers=headers)
    en = '翻译出错'
    if response.status_code == 200:
        en = response.json()['translation'][0].replace('"', "'")
    return en
