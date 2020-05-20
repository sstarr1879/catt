# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 13:30:13 2018

@author: sarah
"""
import os
#import hashlib
from hashlib import md5 
import shutil
import sys

def remove_duplicates(dir):
    
    unique = []
    for filename in os.listdir(dir):
        if os.path.isfile(filename):
            filehash = hashlib.md5(open(filename, 'rb').read()).hexdigest()

          #  filehash = md5.md5(file(filename).read()).hexdigest()
        if filehash not in unique: 
            unique.append(filehash)
        else: 
            shutil.move(filename, 'duplicate_files')            

def main(dir):
    duplicate_files = r'duplicate_files'
    if not os.path.exists(duplicate_files):
        os.makedirs(duplicate_files)
    
    remove_duplicates(os.path.dirname(sys.argv[0]))
    