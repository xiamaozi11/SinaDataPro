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

'''data={'state':[1,1,2,2,1,2,2],'pop':['a','b','c','d','b','c','d'],'score':[55,41,43,41,42,43,42]}  
frame=pd.DataFrame(data)    
p = frame.drop_duplicates(subset=['pop'])'''  

df = GTASys.CSV('data.csv')
'''df =  pd.read_csv('E:\SinaAStocks.csv')
df['commentInfo'] = pd.Series(df['title'].astype(str)+' '+df['content'].astype(str))
data = df.drop_duplicates(subset=['commentInfo'])'''
data1 = df.removeDuplicatedContentItem(filePath = 'data.csv',contentItem = 'content')
#GTASys.CSV.dataFrame_to_xlsx(data1,'E:\SinaAStocks.xlsx')
#data1.to_csv('E:\SinaAStocks1.csv', encoding='utf-8')
data1.index = range(len(data1))
#df = pd.read_csv('E:\SinaAStocks1.csv', encoding='utf-8')
data = copy.deepcopy(data1)
data['A'] = pd.Series(data1['title'].astype(str)+' '+data1['content'].astype(str))
data2 = copy.deepcopy(data)
data3 = copy.deepcopy(data)
wordConvertDict = {}
wordConvertDict = GTASys.Participle.get_dict('stk_Convert.txt')
keyWordList = []
keyWordList = GTASys.Participle.get_list('stk_KeyValue.txt')
stopwords = GTASys.Participle.stopwordsList("stopword.dic")  # 这里加载停用词的 路径  
strKey = '微信'
jieba.add_word(strKey,20000)
jieba.load_userdict("stk_slang.txt")

resultData = pd.DataFrame(columns = ["stockID","stockName", "title", "content", "time", "userID", "url", "isVip"])


index = 0
data3.index = range(len(data3))
#data2.index = range(len(data2))
for i in range(len(data3)):
    string = data3['A'][i]
    s = str(string)
    sList = GTASys.Participle.wordConvert(s.strip(), wordConvertDict,stopwords)
    while ' ' in sList:
        sList.remove(' ')
    cutString =  ''.join(sList)
    cutString.replace(' ','')
    wlist = list(jieba.cut(cutString))
    if(GTASys.Participle.getKeyValue(wlist, keyWordList)) or strKey in wlist:
        data3 = data3.drop(i)

'''for i in range(len(data2)):
    if data2['A'][i] == '':
        data2 = data2.drop(i)'''
data3.to_csv('data.csv')