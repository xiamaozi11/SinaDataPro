# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 08:57:51 2018

@author: maojin.xia
"""

import numpy as np
import pandas as pd
import GTASys
import jieba
import copy
import re

'''data={'state':[1,1,2,2,1,2,2],'pop':['a','b','c','d','b','c','d'],'score':[55,41,43,41,42,43,42]}  
frame=pd.DataFrame(data)    
p = frame.drop_duplicates(subset=['pop'])'''  

df = GTASys.CSV('E:\SinaAStocks1012.csv')
'''df =  pd.read_csv('E:\SinaAStocks.csv')
df['commentInfo'] = pd.Series(df['title'].astype(str)+' '+df['content'].astype(str))
data = df.drop_duplicates(subset=['commentInfo'])'''
data1 = df.removeDuplicatedContentItem(filePath = 'E:\SinaAStocks1012.csv',contentItem = 'content')
GTASys.CSV.dataFrame_to_xlsx(data1,'E:\SinaAStocks1012.xlsx')
#data1.to_csv('E:\SinaAStocks1.csv', encoding='utf-8')
data1.index = range(len(data1))
#df = pd.read_csv('E:\SinaAStocks1.csv', encoding='utf-8')
data = copy.deepcopy(data1)
def T2S(sentence):
    sentence = str(sentence)
    sentence =sentence.replace(' ','')
    #sentence = re.sub('\s','',sentence)
    return sentence
data['content'].apply(lambda s: GTASys.Participle.sentenceEmptyStrConvert(s))
#data['content'].replce(' ','')
data['A'] = pd.Series(data['title'].astype(str)+' '+data['content'].astype(str))

data2 = copy.deepcopy(data)
data3 = copy.deepcopy(data)
wordConvertDict = {}
wordConvertDict = GTASys.Participle.get_dict('stk_Convert.txt')
keyWordList = []
keyWordList = GTASys.Participle.get_list('stk_KeyValue.txt')
stopwords = GTASys.Participle.stopwordsList("stopword.dic")  # 这里加载停用词的路径  
strKey = '微信'
jieba.add_word(strKey,20000)
jieba.load_userdict("stk_slang.txt")

resultData = pd.DataFrame(columns = ["stockID","stockName", "title", "content", "time", "userID", "url", "isVip"])

'''for i in range(len(data3)):
    ti = data3['time'][i]
    string = str(ti)
    wlist = list(jieba.cut(string))
    if '分钟' in wlist or '秒' in wlist:
        #resultData.append(data3[i])     
    #else:
        data3 = data3.drop(i)'''



index = 0
data.index = range(len(data))
#data2.index = range(len(data2))
for i in range(len(data)):
    string = data['A'][i]
    bo = False
    ti = data['time'][i]
    timeValue = str(ti)
    timelist = list(jieba.cut(timeValue))
    if '分钟' in timelist or '秒' in timelist:
        bo = True
    s = str(string)
    sList = GTASys.Participle.wordConvert(s, wordConvertDict,stopwords)
    cutString =  ''.join(sList)
    wlist = list(jieba.cut(cutString))
    if((GTASys.Participle.getKeyValue(wlist, keyWordList)) or strKey in wlist) and bo:
        data = data.drop(i)

'''for i in range(len(data2)):
    if data2['A'][i] == '':
        data2 = data2.drop(i)'''
data.to_csv('sinaAStocksDataGTA2018-10-12.csv', encoding="utf-8", index=False)
data.to_excel('sinaAStocksDataGTA2018-10-12.xlsx', sheet_name='data')