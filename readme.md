# similarity_check

This project is for checking similarities of documents, using TfIdf and LSI model.

### Pre Work

Install python package `gensim` for training model, `jieba` for words segmentation and `pdfminer` for transfer pdf file to txt file.

Add two folders `seg` and `txt` in the root directory for the system to run.

### Usage

The main interface is in main.py. 

Use the following order:

	python main.py --input './data/' --topic_num 10 --border 0.7 --output output.txt
	

* input: input folder of documents to be checked, with files in **PDF** format
* topic_num: num of topic used in LSI model
* border: the similarity of two documents above border will be recorded in the output file
* output: output file name

Then look up the output file to see the similarities of documents.


