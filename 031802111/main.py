import sys
import jieba
import time
import logging
import numpy as np
import codecs
from jieba import analyse
from gensim import corpora,models,similarities
from collections import defaultdict

#输入文本
def call_input(text):
    doc=open(text,'r',encoding="utf-8")
    str_doc=doc.read()
    doc.close()
    return str_doc



#主程序
if __name__ == '__main__':
    str1=call_input(sys.argv[1])
    str2=call_input(sys.argv[2])

    #建立停用词
    stop_words=['。','，','!','?','……']
    #进行分词
    str1_list=[]
    for line in str1:
        str1_words=' '.join(jieba.cut(line)).split(' ')
        doc_txt=[]
        for word in str1_words:
            if word not in stop_words:
                doc_txt.append(word)
        str1_list.append(doc_txt)      

    str2_words=' '.join(jieba.cut(str2)).split(' ')
    str2_list=[]
    for word in str2_words:
        if word not in stop_words:
            str2_list.append(word)

    #对原文进行处理，形成词袋
    dictionary=corpora.Dictionary(str1_list)
    #对词袋中的词进行编号
    dictionary.keys()
    #使用doc2bow制作语料库
    corpus=[dictionary.doc2bow(word) for word in str1_list]
    #对测试文档也进行制作语料库
    test_words_vec=dictionary.doc2bow(str2_list)
    #利用tfidf模型对语料库建模
    tfidf=models.TfidfModel(corpus)
    #对每个目标文档，分析测试文档的相似度
    index=similarities.SparseMatrixSimilarity(tfidf[corpus],num_features=len(dictionary.keys()))
    sim=index[tfidf[test_words_vec]]
    print('相似度为%s','%.2f'% max(sim))
    output_txt=open(sys.argv[3],'w', encoding='utf-8')
    output_txt.write(str('%.2f'% max(sim)))
    output_txt.close()
