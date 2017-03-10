#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2017/2/28
# @Author   : xuziru
# @File     : function.py.py
# @Function : functions used in main.py

import os
import jieba.posseg as pseg
from gensim import corpora, models, similarities


def seg_files():
    input_files = os.listdir('./txt/')
    for i in input_files:
        temp = open('./txt/' + i, 'r').readlines()
        segs = open('./seg/segs_' + i, 'w')
        for j in temp:
            # words = [(i[0].encode('utf-8'), i[1])
            #          for i in analyse.extract_tags(j, topK=10000, withWeight=True, allowPOS=())]
            words = []
            for word, flag in pseg.cut(j):
                # x = '标点', m = '量词', nr = '人名', 'uj' = '的'
                # stopwords can be added here
                if flag not in ['x', 'm', 'nr', 'uj'] and word != '':
                    words.append((word.encode('utf-8'), flag))
            for word in words:
                segs.write(word[0].lower() + ' ' + str(word[1]) + '\n')
    return


def generate_corpora():
    seg_files = os.listdir('./seg/')

    # get seg results from file
    terms_seg = []
    for i in seg_files:
        text = []
        temp = open('./seg/' + i, 'r').readlines()
        for j in temp:
            text.append(j.split(' ')[0])
        terms_seg.append(text)

    # delete words which occurred just once
    all_terms = sum(terms_seg, [])
    terms_once = set(term for term in set(all_terms) if all_terms.count(term) == 1)
    texts = [[term for term in text if term not in terms_once] for text in terms_seg]

    return texts


def generate_model_and_calc_similarity(model_file, texts, topic_num):
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]

    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]

    # model not saved
    #tfidf.save(model_file)

    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=topic_num)
    index = similarities.MatrixSimilarity(lsi[corpus])

    return dictionary, lsi, index
