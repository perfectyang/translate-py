import re, json, requests, uuid, hashlib
from langconv import *
from fake_useragent import UserAgent
ua = UserAgent()
headers={"User-Agent": ua.random}
md = hashlib.md5()
# 繁体翻译
def Simplified2Traditional(sentence):
    sentence = Converter('zh-hant').convert(sentence)
    return sentence

def translate(text, category):
  # url = 'http://fanyi.youdao.com/openapi.do?keyfrom=node-fanyi&key=110811608&type=data&doctype=json&version=1.1&q={}'.format(text)
  data = {
    'gb': Simplified2Traditional(text),
  }
  if category == 'en':
      url = 'http://api.fanyi.baidu.com/api/trans/vip/translate?appid=20190315000277522&from=auto&q={}&to={}&salt={}&sign={}'.format(text, category, salt, sign)
      response = requests.get(url=url, headers=headers).json()
      print('请求回来', response)
      data['en'] = response['translation'][0].replace('"', "'")
  return data

with open('./cloud2.js', 'r+', encoding='utf8') as file:
    content = file.read()
    con = re.search(r'({.*})', content, re.S).group().replace("'", '"')
    newContent = re.sub(r"(\w*):\B", lambda m: '"'+ m.group(1) + '":', con)
    print('newContent', newContent)
    originconfig = json.dumps(json.loads(newContent), indent = 2, ensure_ascii=False)
    enconfig = json.loads(originconfig)
    gbconfig = json.loads(originconfig)


def readFile(config, params, category = 'en'):
    for key in config:
        if type(config[key]).__name__ == 'dict':
            readFile(config[key], params, category)
        else:
            params[key] = translate(config[key], category)[category]
            config[key] = translate(config[key], category)[category]

contenObj = {}

# readFile(enconfig, contenObj, 'en')
readFile(gbconfig, contenObj, 'gb')
#
# print('中文版', originconfig)
# print('英文版', json.dumps(enconfig, indent = 4, ensure_ascii=False))
# print('繁体版', json.dumps(gbconfig, indent = 4, ensure_ascii=False))

# readFile(enconfig, contenObj, 'en')
readFile(gbconfig, contenObj, 'gb')

def linkJs(enV):
    return 'export const {} = '.format(enV)

with open('./cloud3.js', 'w+', encoding='utf8') as contentF:
    allContent = linkJs('zh') + originconfig + '\n' + linkJs('en') + json.dumps(enconfig, indent = 2, ensure_ascii=False) + '\n' + linkJs('GB') + json.dumps(gbconfig, indent = 2, ensure_ascii=False) + '\n' + 'export default {zh, en, GB}'
    contentF.write(allContent.replace('"', "'"))
