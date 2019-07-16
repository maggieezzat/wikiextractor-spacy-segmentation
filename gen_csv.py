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

def gen_dewiki_csvs(rootdir = dir, output="/bert/dewiki_csv_files/"):

    directory = os.path.dirname(output)
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




def gen_tfrecords_csv(rootdir = dir, output="/bert/bert-german/vocab/dewiki_lower_128.csv"):

    files = [
        f
        for f in listdir(rootdir)
        #if isfile(join(rootdir, f))
    ]

    csv = []
    for file in files:
        #file_path = join(rootdir, file)
        file_path = "/bert/tfrecords/"+file+".tfrecord"
        csv.append(file_path)

    with open(output, 'w') as f:
        for item in csv:
            f.write(item + '\n')




def main():
    #gen_csv_file()
    #gen_tfrecords_csv()


if __name__ == "__main__":
    main()
