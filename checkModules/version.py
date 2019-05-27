import os
import re
import sys
import json
from threading import Thread as moreline

def reccord(url, recordVs):
    with open(url, 'r+', encoding='utf8') as files:
        allContent = json.loads(files.read())
        tem = {
            "url": url
        }
        temname = ''
        temvs = ''
        if 'name' in allContent.keys():
            tem["name"] = allContent["name"]
            temname = 'name'
        if "version" in allContent.keys():
            tem["version"] = allContent["version"]
            temvs = 'version'
        if temname == '':
            tem['name'] = 'none'
        if temvs == '':
            tem['version'] = 'none'
        print('记录下来:', tem)
        recordVs.append(tem)
#遍历文件夹
def iter_files(rootDir, allUrl):
    #遍历根目录
    for files in os.listdir(rootDir):
        curFiles = os.path.join(rootDir, files)
        if os.path.isdir(curFiles) and not curFiles.endswith('node_modules'):
            iter_files(curFiles, allUrl)
        elif os.path.isfile(curFiles) and curFiles.endswith('package.json'):
            print('开始分析package.json', curFiles)
            allUrl.append(curFiles)
# 多线程
def multiline(allUrl, recordVs):
    lineT = []
    for url in allUrl:
        t = moreline(target=reccord, args=(url, recordVs))
        t.start()
        lineT.append(t)
    for l in lineT:
        l.join()

def startCheck (packagePath):
    recordVs = []
    allUrl = []
    iter_files(packagePath, allUrl)
    multiline(allUrl, recordVs)
    print('----------分析完成------------')
    print('总数package.json:', len(allUrl))
    print('记录总数:', len(recordVs))
    return recordVs



# with open(args[2], 'w+', newline=None) as allFiles:
#     allFiles.write(str(recordVs))
