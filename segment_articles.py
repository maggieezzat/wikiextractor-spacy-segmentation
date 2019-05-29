# coding=utf-8

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
from os import listdir, remove
from os.path import isfile, join
import sys
from absl import app as absl_app
import tensorflow as tf
import spacy
import csv


dir = "/home/maggie/german-articles-data/articles_train.tsv"
out_dir = "/home/maggie/german-articles-data/pretraining_articles.txt"

def text_cleaning(rootdir=dir, output_root=out_dir):

    nlp = spacy.load('de_core_news_sm')

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
                            

def main(_):
    text_cleaning()


if __name__ == "__main__":
    absl_app.run(main)