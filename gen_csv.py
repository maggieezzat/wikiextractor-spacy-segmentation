# coding=utf-8

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
from os import listdir, remove
from os.path import isfile, join
import sys
import string

dir = "/bert/bert_dewiki_cleaned/"
out = "/bert/dewiki_csv_files/"

def gen_csv_file(rootdir=dir, output=out):

    directory = os.path.dirname(rootdir)
    if not os.path.exists(directory):
        os.makedirs(directory)

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


def main():
    gen_csv_file()


if __name__ == "__main__":
    main()
