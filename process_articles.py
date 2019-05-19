# coding=utf-8

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import codecs
import fnmatch
import os
from os import listdir, remove
from os.path import isfile, join
import sys
import unicodedata
from absl import app as absl_app
import tensorflow as tf

import string
import collections

import spacy
import csv


dir = "/home/maggie/articles/articles_train.tsv"
out_dir = "/home/maggie/pretraining_articles.txt"

def text_cleaning(rootdir=dir, output_root=out_dir):

    nlp = spacy.load('de_core_news_sm')

    with tf.gfile.Open(rootdir, "r") as f:
        with open(output_root, 'w', encoding='utf-8') as new_file:
            reader = csv.reader(f, delimiter="\t", quotechar=None)
            lines = []
            for line in reader:
               lines.append(line)
            lines = lines[1:]

            for line in lines:
                doc = line[3]
                doc = nlp(doc)
                sentences = list(doc.sents)
                for i in range(len(sentences)):
                    new_file.write(sentences[i].string.strip() + '\n')
                new_file.write('\n')
                doc = ""
                            

def main(_):
    text_cleaning()


if __name__ == "__main__":
    absl_app.run(main)