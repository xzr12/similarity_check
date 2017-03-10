#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2017/3/6
# @Author   : xuziru
# @File     : pdf2txt.py
# @Function : convert pdf file to txt
# reference : chenbjin(http://www.cnblogs.com/chenbjin/p/3837453.html)

import os
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


def pdf2txt(filename):
    outfile = './txt/' + filename.split('/')[2] + '.txt'
    debug = 0
    pagenos = set()
    password = ''
    maxpages = 0
    rotation = 0
    codec = 'utf-8'  # 输出编码
    caching = True
    imagewriter = None
    laparams = LAParams()

    PDFResourceManager.debug = debug
    PDFPageInterpreter.debug = debug

    rsrcmgr = PDFResourceManager(caching=caching)
    outfp = file(outfile, 'w')

    # pdf转换
    device = TextConverter(rsrcmgr, outfp, codec=codec, laparams=laparams, imagewriter=imagewriter)
    fp = file(filename, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    # 处理文档对象中每一页的内容
    for page in PDFPage.get_pages(fp, pagenos,
                                  maxpages=maxpages, password=password,
                                  caching=caching, check_extractable=True):
        page.rotate = (page.rotate + rotation) % 360
        interpreter.process_page(page)

    fp.close()
    device.close()
    outfp.close()
    return


