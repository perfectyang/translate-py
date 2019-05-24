# from baidu import translateEnglish
# import re, random, os
# # with open('./newzh.js', 'r+', encoding='utf8') as f:
# #     content = f.read()
# #     con = re.search(r'({.*})', content, re.S).group()
# #     subs = re.sub(r'\s*(\/\/.*?)\n',lambda x: '\n', con, re.S)
# #     print('con', con)
# #     print(subs)
# count = random.randint(1, 3)
# print(count)

from googletrans import Translator
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )
translator = Translator()
print(translator.translate('今天天气不错').text)
print translator.translate('今天天气不错', dest='ja').text
print translator.translate('今天天气不错', dest='ko').text
