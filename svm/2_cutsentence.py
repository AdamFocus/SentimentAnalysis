#!/usr/bin/env python
# -*- coding: utf-8  -*-
#逐行读取文件数据进行jieba分词
import jieba
import jieba.analyse
import codecs,sys,string,re
# 文本分词
def prepareData(sourceFile,targetFile):
    f = codecs.open(sourceFile, 'r', encoding="utf-8")
    target = codecs.open(targetFile, 'w',encoding="utf-8")
    print('open source file: '+ sourceFile)
    print('open target file: '+ targetFile)

    lineNum = 1
    line = f.readline()
    while line:
        print('---processing ',lineNum,' article---')
        #去除文本中的符号等
        line = clearTxt(line)
        seg_line = sent2word(line)
        target.write((seg_line + '\n'))
        lineNum = lineNum + 1
        line = f.readline()
    print('well done.')
    f.close()
    target.close()

# 清洗文本
def clearTxt(line):
    if line != "":
        #去空格
        line = line.strip()
        intab = ""
        outtab = ""

        #前者为所有的标点，后者为所有的数字
        pun_num = string.punctuation + string.digits
        #line = line.encode('utf-8')
        trantab = str.maketrans(intab, outtab,pun_num)
        line = line.translate(trantab)
       # line = line.decode("utf8")

        #去除文本中的英文和数字
        line = re.sub("[a-zA-Z0-9]","",line)
        #去除文本中的中文符号和英文符号
        line = re.sub("[\s+\.\!\/_,$%^*(+\"\'；：“”．]+|[+——！，。？?、~@#￥%……&*（）]+", "",line)
    return line

#文本切割
def sent2word(line):
    segList = jieba.cut(line,cut_all=False)    
    segSentence = ""
    for word in segList:
        if word != '\t':
            segSentence += word + " "
    return segSentence.strip()

if __name__ == '__main__':   
    sourceFile = '2000_neg.txt'
    targetFile = '2000_neg_cut.txt'
    prepareData(sourceFile,targetFile)
    sourceFile = '2000_pos.txt'
    targetFile = '2000_pos_cut.txt'
    prepareData(sourceFile,targetFile)
