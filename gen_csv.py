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

dir = "/home/maggie/spacy_processed_text"
#dir = "/media/maggie/New Volume/spacy_processed_text"

#out = "/media/maggie/New Volume/csv_files"
out = "/home/maggie/csv_files"

def gen_csv_file(rootdir=dir, output=out):

    if not tf.gfile.Exists(output):
        tf.gfile.MakeDirs(output)

    paths = listdir(rootdir)
    

    for path in paths:

        csv = []
        files = [
            f
            for f in listdir(join(rootdir, path))
            if isfile(join(rootdir, path, f))
        ]

        for file in files:
            file_path = join(rootdir, path, file) 
            csv.append(file_path)

        output_file = join(out, path + ".csv")
        with open(output_file, 'w') as f:
            for item in csv:
                f.write(item + '\n')


def main(_):
    gen_csv_file()


if __name__ == "__main__":
    absl_app.run(main)
