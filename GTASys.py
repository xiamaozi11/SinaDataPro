# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 08:45:13 2018

@author: maojin.xia
"""
import pandas as pd
import copy
import jieba
import re

class CSV:
    def __init__(self,filePath):
        self.df = pd.read_csv(filePath)
          
    def removeDuplicatedContentItem(self,filePath,contentItem):
        df =  pd.read_csv(filePath)
        data = df.drop_duplicates(subset=[contentItem])  
        return data
    
    def csv_to_xlsx_pd(self,filePath,newFilePath):
        csv = pd.read_csv(filePath, encoding='utf-8')
        csv.to_excel(newFilePath, sheet_name='data')
    
    def dataFrame_to_xlsx(df,newFilePath):
        df.to_excel(newFilePath, sheet_name='data')
          

class Excel:
    def __init__(self,filePath):
        self.df = pd.read_csv(filePath)
        
    def removeDuplicatedContent(self,filePath,contentItem):
        df =  pd.read_excel(filePath)
        data = df.drop_duplicates(subset=[contentItem])  
        return data
    
    def xlsx_to_csv_pd(self,filePath,newFilePath):
        csv = pd.read_excel(filePath, index_col=0)
        csv.to_csv(newFilePath, encoding='utf-8')


class Participle:
    
    def wordConvert(sentence,wordConvertDict,stopwords):
        #string = '兄弟，我也云南的，你的优惠也挺大的，现在哪里来的全系3万啊。。。现傲虎全系无优惠，森林人才八千'
        string = sentence
        s1 = copy.deepcopy(string)
        
        sList = list(jieba.cut(s1,HMM=False))
        rep = [wordConvertDict[s] if s in wordConvertDict.keys() else s for s in sList]
        wordList = []
        sList = rep
        for word in sList:
            if word not in stopwords:  
                if word != '\t':
                    wordList.append(word)
        
        return wordList
    
    def sentenceEmptyStrConvert(sentence):
        string = str(sentence)
        sList = list(jieba.cut(string,HMM = False))
        #s = filter(None, sList)
        sList = [x for x in sList if x != '\u3000']
        sList = [x for x in sList if x != ' ']
        s = ''.join(sList)
        return s

    def stopwordsList(filepath):  
        stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]  
        return stopwords 
    
    def get_dict(path, encoding="utf-8-sig"):
        sentiment_dict = {}
        pattern = re.compile(r"\s+")
        with open(path, encoding=encoding) as f:
             for line in f:
                 result = pattern.split(line.strip())
                 if len(result) == 2:
                     sentiment_dict[result[0]] = result[1]
        return sentiment_dict
    
    def get_list(path, encoding="utf-8-sig"):
        sentiment_list = []
        pattern = re.compile(r"\s+")
        with open(path, encoding=encoding) as f:
             for line in f:
                 result = pattern.split(line.strip())
                 if len(result) == 1:
                     sentiment_list.append(result[0])
        return sentiment_list
    
    def getKeyDicValue(sList, keyDict):
        for s in sList:
                if s in keyDict.keys():
                    return keyDict[s]
        return ''
    
    def getKeyValue(sList, keyList):
        for s in sList:
                if s in keyList:
                    return True
        return False