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
import string
import collections

import nltk
from nltk.tokenize import sent_tokenize

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from clean_text import clean_sentence



dir = "/lm_corpus/dewiki_extracted/"
out_dir = "/lm_corpus/dewiki_spacy_segmented/"

def tokenize_into_sents(rootdir=dir, output_root=out_dir):

    paths = listdir(rootdir)

    exists = os.path.isdir(output_root)
    if not exists:
        os.mkdir(output_root)

    total_paths = len(paths)
    current_path = 0 

    for path in paths:

        output_dir = join(output_root, path)
        exists = os.path.isdir(output_dir)
        if not exists:
            os.mkdir(output_dir)
    
        files = [
            f
            for f in listdir(join(rootdir, path))
            if isfile(join(rootdir, path, f))
        ]

        current_path+=1
        total_files = len(files)
        processed_files = 0

        for file in files:

            file_path = join(rootdir, path, file) 
            new_file_name = join(output_dir, file + "_ntlk.txt")

            processed_files+=1
            print("Processing path " + path + " " +  str(current_path) +  "/" + str(total_paths)
            + " Files: " + str(processed_files) + "/" + str(total_files), end="\r")

            with open(file_path, 'r+', encoding='utf-8') as f:
                with open(new_file_name, 'w', encoding='utf-8') as new_file:
                    content = f.readlines()
                    doc = ""
                    for i in range(len(content)):
                        if "<doc id=" in content[i] or not content[i].strip():
                            i+=1
                            continue
                        if "</doc>" in content[i]:
                            #doc = nlp(doc)
                            #sentences = list(doc.sents)
                            sentences = sent_tokenize(doc)
                            for j in range(len(sentences)):
                                #clean_sent = clean_sentence(sentences[j])
                                #new_file.write(clean_sent + '\n')
                                new_file.write(sentences[j] + '\n')
                            new_file.write('\n')
                            doc = ""
                        else:
                            doc = doc + content[i]

                exit()
                            

def main():
    tokenize_into_sents()


if __name__ == "__main__":
    main()