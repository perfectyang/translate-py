import re, json, requests
from langconv import *
from baidu import translateEnglish
import time, random
# 繁体翻译
def Simplified2Traditional(sentence):
    sentence = Converter('zh-hant').convert(sentence)
    return sentence
# 英文翻译
def translate(text, category):
    data = {
      'gb': Simplified2Traditional(text),
    }
    if category == 'en':
        print('translate to start ---{}'.format(text))
        data['en'] = translateEnglish(text)
        print('finished to translate-{0}--{1}'.format(text, data['en']))
        countTime = random.randint(1, 3)
        print('waiting for {} second to start translate in case that interface have been banned'.format(countTime))
        time.sleep(countTime)
    return data

with open('./testnewzh.js', 'r+', encoding='utf8') as file:
    content = file.read()
    newContent = re.search(r'({.*})', content, re.S).group().replace("'", '"')
    print('原数据', newContent)
    # 去除js里面的注释
    handleConfig = re.sub(r'\s*(\/\/.*?)\n',lambda x: '\n', newContent, re.S)
    noMarkOriginconfig = json.dumps(json.loads(handleConfig), indent = 2, ensure_ascii=False)
    enconfig = json.loads(noMarkOriginconfig)
    gbconfig = json.loads(noMarkOriginconfig)

def readFile(config, category = 'en'):
    for key in config:
        if type(config[key]).__name__ == 'dict':
            readFile(config[key], category)
        else:
            config[key] = translate(config[key], category)[category]

readFile(enconfig, 'en')
readFile(gbconfig, 'gb')

def linkJs(enV):
    return 'export const {} = '.format(enV)

with open('./newzh3.js', 'w+', encoding='utf8') as contentF:
    allContent = linkJs('zh') + newContent + '\n' + linkJs('en') + json.dumps(enconfig, indent = 2, ensure_ascii=False) + '\n' + linkJs('GB') + json.dumps(gbconfig, indent = 2, ensure_ascii=False) + '\n' + 'export default {zh, en, GB}'
    contentF.write(allContent.replace('"', "'"))
