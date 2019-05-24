from langconv import *

def Simplified2Traditional(sentence):
    sentence = Converter('zh-hant').convert(sentence)
    return sentence