#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2017/2/28
# @Author   : xuziru
# @File     : main.py
# @Function : main interface for document comparision

import argparse
import logging
from function import *
from pdf2txt import *


def parse_args():
    parser = argparse.ArgumentParser(description='Compare')
    parser.add_argument('--folder', type=str, default='./data/', help='documents folder')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    folder = args.folder

    # pre process
    files = os.listdir(folder)
    for i in files:
        pdf2txt(folder + i)
    logging.info('transfer pdf->txt finish')

    seg_files()
    logging.info('seg files finish')

    # construct model and compute similarity
    texts = generate_corpora()
    dictionary, lsi, index = generate_model_and_calc_similarity('./test.tfidf_model', texts, 10)
    test = texts[0]
    test_bow = dictionary.doc2bow(test)
    test_lsi = lsi[test_bow]
    sims = index[test_lsi]
    sorted_sims = sorted(enumerate(sims), key=lambda item: -item[1])
    print sorted_sims[0:10]

    # output result to file

    logging.info('process finish')
