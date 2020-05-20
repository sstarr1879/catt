# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 12:46:55 2018

@author: sarah
"""

import os 
import sys 
import shutil

import hashlib
import time

#helper functions to do stuff
#function to open all the images


#helper function to find duplicates
def move_duplicates(dir):
    
    unique = []
    for filename in os.listdir(dir):
        if file == 'duplicate_files':
            filetype = 'folder'
        elif file == 'exception_files':
                filetype = 'folder'
        
        else:
            if os.path.isfile(filename):
                filehash = hashlib.md5(open(filename, 'rb').read()).hexdigest()
    
              #  filehash = md5.md5(file(filename).read()).hexdigest()
            if filehash not in unique: 
                unique.append(filehash)
            else: 
                try: 
                    shutil.move(filename, 'duplicate_files') 
                except: 
                    shutil.move(filename, 'exception_files')

#main function that walks through the files
def main():

    #set current folder as working directory (for local dev)
 #   os.chdir(os.path.dirname(sys.argv[0]))
    print('#########################################################################')
    print('##                                                                     ##')   
    print('##          ** WELCOME TO IMAGE SORTING CATT **                        ##')                                                  ##')      
    print('##                      BETA                                           ##') 
    print('##                                                                     ##')                  
    print('#########################################################################')
    
 #executable version path
    dirname, filename = os.path.split(os.path.abspath(__file__))
    #create new folders to store images that we most likely don't need
    print('image files to sort:', len(os.listdir('.')))    
    
 #  duplicate_files = r'duplicate_files' 
  # if not os.path.exists(duplicate_files):
   #    os.makedirs(duplicate_files)
        
#call the remove_duplicates function to move the duplicates

    exception_files = r'exception_files' 
    if not os.path.exists(exception_files):
        os.makedirs(exception_files)

    
#main loop through the files to move them
    
    
    files = [file for file in os.listdir(u'.')]
 #   print(len(files))
  #  input_var = input("Enter desired batchsize: ")
  #  batchsize = int(input_var)
  
    batchsize = 1000
     #user input batchsize or default to len(files/10)
 #   default_batches = int(len(file)/ 10)
  #  batchsize = input("Enter desired batchsize or press enter for default : ") or default_batches

 
    print ("user-specified batch size:", batchsize) 
    
   

    index = 0
    remaining = len(files)
    print('your job will be completed in the following batches:', (len(files)/batchsize))
    start_time = time.time()
    print('STARTING')
    print('START_TIME:', start_time)
    
    print('-------------------------------------------------------------------------')
#    print('Removing Duplicate Files....')
 #   move_duplicates(dirname)
  #  print('Duplicates moved.')
   # time_one = time.time()
    #print('Time to move duplicates:', time_one-start_time)
    #print('-------------------------------------------------------------------------')
    print('SORTING IMAGE FILES...')
    
    embedded_images = r'embedded_images' 
    if not os.path.exists(embedded_images):
        os.makedirs(embedded_images)
        
    thumbnails = r'thumbnails' 
    if not os.path.exists(thumbnails):
        os.makedirs(thumbnails)
    
    cached_images = r'cached_images' 
    if not os.path.exists(cached_images):
        os.makedirs(cached_images)
    
    triage_files = r'triage_files' 
    if not os.path.exists(triage_files):
        os.makedirs(triage_files)
    
    exception_files = r'exception_files' 
    if not os.path.exists(exception_files):
        os.makedirs(exception_files)

    while remaining > 0:
        batch = min(remaining, batchsize)
        print('Now working on Batch:', (index/batchsize))
        for file in files[index:index+batch]:    
    
#        for file in os.listdir("."):
        #check for small images
            if file.endswith("py"):
                filetype = 'python_script' #don't touch the py script
            elif file.endswith("exe"):
                filetype = 'execution_file' #don't touch the py script
            elif file == 'embedded_images':
                filetype = 'folder'
            elif file == 'exception_files':
                filetype = 'folder'
            elif file == 'thumbnails':
                filetype = 'folder'
            elif file == 'cached_images':
                filetype = 'folder'
            elif file == 'triage_files':
                filetype = 'folder'
            elif file == 'duplicate_files': #don't touch the file we created
                filetype = 'folder'
            elif 'embed' in file:
                try:
                    shutil.move(file, 'embedded_images')
                except: 
                    shutil.move(file, 'exception_files')
            elif 'Embed' in file:
                try:
                    shutil.move(file, 'embedded_images')
                except: 
                    shutil.move(file, 'exception_files')
            elif 'cache' in file:
                try:
                    shutil.move(file, 'cached_images')
                except: 
                    shutil.move(file, 'exception_files')
            elif os.path.getsize(file) < 50 * 1024: #check if image is less than 50kn
                try:
                    shutil.move(file, 'thumbnails')
                except: 
                    shutil.move(file, 'exception_files')
            else: 
                try:
                    shutil.move(file, 'triage_files')
                except: 
                    shutil.move(file, 'exception_files')
            
        index += batch
        remaining -= batch
        
    end_time = time.time()
    
    print('TOTAL TIME TO COMPLETE:', end_time - start_time)

main()

