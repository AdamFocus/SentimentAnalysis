#!/usr/bin/env python
# -*- coding: utf-8  -*-
#从词向量模型中提取文本特征向量
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')# 忽略警告
import logging
import os.path
import codecs,sys
import numpy as np
import pandas as pd
import gensim

# 返回特征词向量
def getWordVecs(wordList,model):
    vecs = []
    for word in wordList:
        word = word.replace('\n','')
        #print word
        try:
            #对于每一行的word在训练好的词向量模型中匹配
            vecs.append(model[word])
        except KeyError:
            continue
    return np.array(vecs, dtype='float')
    

# 构建文档词向量 
def buildVecs(filename,model):
    fileVecs = []
    i=0
    with codecs.open(filename, 'rb', encoding='utf-8') as contents:
        for line in contents:
            logger.info("Start line: " + line)
            wordList = line.split(' ')
            vecs = getWordVecs(wordList,model)
            #print vecs
            #sys.exit()
            #计算均值
            # for each sentence, the mean vector of all its vectors is used to represent this sentence
            if len(vecs) >0:
                vecsArray = sum(np.array(vecs))/len(vecs) # mean
                #print vecsArray
                #sys.exit()
                fileVecs.append(vecsArray)
            else:
                i+=1
    print(i)
    return fileVecs   

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))
    
    # load word2vec model
    #使用已经训练好的词向量模型
    #fdir = '/Users/sy/Desktop/pyRoot/SentimentAnalysis/'
    fdir = 'G:/MyProject/senti_analysis-master/'
    inp = fdir + 'wiki.zh.text.vector'
    model = gensim.models.KeyedVectors.load_word2vec_format(inp, binary=False)
    
    posInput = buildVecs(fdir + '2000_pos_cut_stopword.txt',model)
    negInput = buildVecs(fdir + '2000_neg_cut_stopword.txt',model)

    #print(len(posInput))
    #print(len(negInput))
    # use 1 for positive sentiment， 0 for negative
    Y = np.concatenate((np.ones(len(posInput)), np.zeros(len(negInput))))

    X = posInput[:]
    for neg in negInput:
        X.append(neg)
    X = np.array(X)

    # write in file
    df_x = pd.DataFrame(X)
    df_y = pd.DataFrame(Y)
    data = pd.concat([df_y,df_x],axis = 1)
    #print data
    data.to_csv(fdir + '2000_data.csv')
    logger.info("ok")

    


