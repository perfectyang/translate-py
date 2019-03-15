import re, json, requests
from langconv import *
from baidu import translateEnglish
import time

# 繁体翻译
def Simplified2Traditional(sentence):
    sentence = Converter('zh-hant').convert(sentence)
    return sentence

def translate(text, category):
    data = {
      'gb': Simplified2Traditional(text),
    }
    if category == 'en':
        data['en'] = translateEnglish(text)['dst']
        # time.sleep(5)
    return data

with open('./newzh.js', 'r+', encoding='utf8') as file:
    content = file.read()
    con = re.search(r'({.*})', content, re.S).group().replace("'", '"')
    newContent = con
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

readFile(enconfig, contenObj, 'en')
readFile(gbconfig, contenObj, 'gb')

def linkJs(enV):
    return 'export const {} = '.format(enV)

with open('./newzh2.js', 'w+', encoding='utf8') as contentF:
    allContent = linkJs('zh') + originconfig + '\n' + linkJs('en') + json.dumps(enconfig, indent = 2, ensure_ascii=False) + '\n' + linkJs('GB') + json.dumps(gbconfig, indent = 2, ensure_ascii=False) + '\n' + 'export default {zh, en, GB}'
    contentF.write(allContent.replace('"', "'"))
