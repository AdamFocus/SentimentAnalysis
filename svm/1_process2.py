#!/usr/bin/env python
# -*- coding: utf-8  -*-
#将原始数据合并到一个txt文件
import logging
import os,sys
import pandas as pd
import csv,codecs

if __name__== '__main__':
    program = os.path.basename(sys.argv[0])  # 得到文件名
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)

    addr1='data\\ChnSentiCorp_htl_ba_2000'
    folder=['neg','pos']

    addr2='data\\ChnSentiCorp_htl_all.csv'
    i1=0
    i2=0
    outp1="2000_neg.txt"
    output1=open(outp1,'w',encoding='utf-8')
    outp2="2000_pos.txt"
    output2 = open(outp2, 'w',encoding='utf-8')
    f=open(addr2,'r',encoding='utf-8')
    f_csv = csv.reader(f)
    headers= next(f_csv)
    print(headers)

    for row in f_csv:
        if row[0]=='0':
            if i1<1000:
                output1.writelines(row[1]+'\n')
                i1+=1
        else:
            if i2<1000:
                i2+=1
                output2.writelines(row[1]+'\n')
    output1.close()
    output2.close()
    logger.info("ok")

