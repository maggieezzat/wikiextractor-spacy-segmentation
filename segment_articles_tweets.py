# coding=utf-8

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
from os import listdir, remove
from os.path import isfile, join
import sys
import tensorflow as tf
import spacy
import csv
import codecs
import fnmatch
import sys
import unicodedata
import string
import collections


nlp = spacy.load('de_core_news_sm')

tw_dir = "/home/maggie/twitter-data/tweets-train.tsv"
tw_out_dir = "/home/maggie/twitter-data/pretraining_tweets.txt"

ar_dir = "/home/maggie/german-articles-data/articles_train.tsv"
ar_out_dir = "/home/maggie/german-articles-data/pretraining_articles.txt"


def tokenize_tweets(rootdir=tw_dir, output_root=tw_out_dir):

    with tf.gfile.Open(rootdir, "r") as f:
        with open(output_root, 'w', encoding='utf-8') as new_file:
            reader = csv.reader(f, delimiter="\t", quotechar=None)
            for line in reader:
                doc = line[1]
                #doc = nlp(doc)
                #sentences = list(doc.sents)
                #for i in range(len(sentences)):
                #    new_file.write(sentences[i].string.strip() + '\n')
                new_file.write(doc + '\n')
                new_file.write('\n')
                doc = ""




def tokenize_articles(rootdir=ar_dir, output_root=ar_out_dir):

    with tf.gfile.Open(rootdir, "r") as f:
        with open(output_root, 'w', encoding='utf-8') as new_file:
            reader = csv.reader(f, delimiter="\t", quotechar=None)
            for line in reader:
                doc = line[1]
                doc = nlp(doc)
                sentences = list(doc.sents)
                for i in range(len(sentences)):
                    new_file.write(sentences[i].string.strip() + '\n')
                new_file.write('\n')
                doc = ""



                            

def main():
    tokenize_tweets()
    tokenize_articles()


if __name__ == "__main__":
    main()

