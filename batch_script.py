# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 16:08:44 2018

@author: sarah
"""

import os
import shutil

def main():
    dirname, filename = os.path.split(os.path.abspath(__file__))
    
    embedded_images = r'embedded_images' 
    if not os.path.exists(embedded_images):
        os.makedirs(embedded_images)
        
    thumbnails = r'thumbnails' 
    if not os.path.exists(thumbnails):
        os.makedirs(thumbnails)
    
    cached_images = r'cached_images' 
    if not os.path.exists(cached_images):
        os.makedirs(cached_images)
    
    files = [file for file in os.listdir(dirname)]
    print(len(files))
    batchsize = 1000
    index = 0
    remaining = len(files)
    print('your job will be completed in the following batches', (len(files)/batchsize))
    while remaining > 0:
        batch = min(remaining, batchsize)
        print('Now working on Batch:', (index/batchsize))
        for file in files[index:index+batch]:
            if file.endswith("py"):
                filetype = 'python_script' #don't touch the py script
            elif file == 'embedded_images':
                filetype = 'folder'
            elif file == 'cached_images':
                filetype = 'folder'
            elif 'embed' in file:
                shutil.move(file, 'embedded_images')
            elif 'cache' in file:
                shutil.move(file, 'cached_images')
            elif os.path.getsize(file) < 50 * 1024: #check if image is less than 50kn
                shutil.move(file, 'thumbnails')
            else: 
                filetype = 'keepfile'
        index += batch
        remaining -= batch
        
main()