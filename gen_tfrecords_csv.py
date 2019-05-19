# coding=utf-8

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
from os import listdir
from os.path import isfile, join
import sys
from absl import app as absl_app

dir = "/media/maggie/Data/spacy_processed_text/"
out = "/home/maggie/dewiki_new_cased_vocab_512_train.csv"



def gen_tfrecords_csv_file(rootdir=dir, output=out):

    files = [
        f
        for f in listdir(rootdir)
        #if isfile(join(rootdir, f))
    ]

    csv = []
    for file in files:
        #file_path = join(rootdir, file)
        file_path = "gs://deep_speech_bucket/dewiki_my_cased_1000vocab_512/"+file+".tfrecord"
        csv.append(file_path)

    with open(output, 'w') as f:
        for item in csv:
            f.write(item + '\n')


def main(_):
    gen_tfrecords_csv_file()


if __name__ == "__main__":
    absl_app.run(main)
