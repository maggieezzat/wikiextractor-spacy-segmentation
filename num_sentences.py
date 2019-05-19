# coding=utf-8

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
from os import listdir, remove
from os.path import isfile, join
import sys
from absl import app as absl_app
import string
import tensorflow as tf

dir = "/media/maggie/Data/spacy_processed_text"
#out = "/home/maggie/num_sentences.txt"
out = "/home/maggie/num_words.txt"

def count_sentences(rootdir=dir, output=out):


    paths = listdir(rootdir)
    sentences_count = 0

    total_paths = len(paths)
    processed_paths = 0

    for path in paths:
        processed_paths+=1

        files = [
            f
            for f in listdir(join(rootdir, path))
            if isfile(join(rootdir, path, f))
        ]

        total_files = len(files)
        processed_files = 0

        for file in files:
            processed_files+=1
            print("Processing Directory: " + str(processed_paths) + "/"
            + str(total_paths) + " Files: "+ str(processed_files) + "/"
            + str(total_files), end='\r')
            file_path = join(rootdir, path, file) 
            with open(file_path, 'r') as f:
                content = f.readlines()
                content = [x.strip() for x in content]
                length = len(content)
                sentences_count += length


    with open(output, 'w') as f:
        f.write("Number of Sentences in German Wikipedia Corpus: "+ str(sentences_count) + '\n')


def count_words(rootdir=dir, output=out):


    paths = listdir(rootdir)
    words_count = 0

    total_paths = len(paths)
    processed_paths = 0

    for path in paths:
        processed_paths+=1

        files = [
            f
            for f in listdir(join(rootdir, path))
            if isfile(join(rootdir, path, f))
        ]

        total_files = len(files)
        processed_files = 0

        for file in files:
            processed_files+=1
            print("Processing Directory: " + str(processed_paths) + "/"
            + str(total_paths) + " Files: "+ str(processed_files) + "/"
            + str(total_files), end='\r')
            file_path = join(rootdir, path, file) 
            with open(file_path, 'r') as f:
                content = f.readlines()
                content = [x.strip() for x in content]
                for sent in content:
                    sent = sent.split()
                    words_count += len(sent)


    with open(output, 'w') as f:
        f.write("Number of Words in German Wikipedia Corpus: "+ str(words_count) + '\n')


def main(_):
    count_words()


if __name__ == "__main__":
    absl_app.run(main)
