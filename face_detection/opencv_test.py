# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 12:53:52 2018

@author: sarah
"""



#import required libraries 
#import OpenCV library
import os
import cv2
import shutil
#import matplotlib library

#importing time library for speed comparisons of both classifiers
 
#%matplotlib inline
#import required libraries 
#import OpenCV library

#os.chdir('C:/Users/sarah/Documents/Python_Scripts/dev_folder/face_detection')
import logging

def convertToRGB(img): 
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def main():
    
    
    logging.basicConfig(filename='opencv_test.log',level=logging.DEBUG, format ='%(asctime)s %(message)s' )


    dirname, filename = os.path.split(os.path.abspath(__file__))
    os.chdir(dirname)

    face_detection = r'face_detection' 
    if not os.path.exists(face_detection):
        os.makedirs(face_detection)
    exception_files = r'exception_files' 
    
    if not os.path.exists(exception_files):
        os.makedirs(exception_files)
        
    try:
        cascPath = 'haarcascade_frontalface_alt.xml'
        logging.info('successfully loaded trained Haar cascade')
    except:
        logging.error('could not find xml for Haar cascade')
          #  cascPath ='C:/Users/sarah/AppData/Local/Continuum/anaconda2/pkgs/opencv/sources/data/haarcascades/haarcascade_frontalface_alt.xml'
       #     cascPath ='C:/Users/sarah/AppData/Local/Continuum/anaconda2/pkgs/opencv/sources/data/haarcascades/haarcascade_fullbody.xml'
            
    faceCascade = cv2.CascadeClassifier(cascPath)
    logging.info('successfully built face Cascade Classifier from path')
       
    for file in os.listdir('.'):
        if file.endswith('jpg'):
            test1 = cv2.imread(file)
            logging.info('loaded file: %s', file)
          #  test1 = cv2.imread('180824-trump-twitter-licensing-people-feature.jpg')
            #convert the test image to gray image as opencv face detector expects gray images 
      #      gray_img = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)
            
            #if you have matplotlib installed then  
        #    plt.imshow(gray_img, cmap='gray')  
             
            # or display the gray image using OpenCV 
            # cv2.imshow('Test Imag', gray_img) 
            # cv2.waitKey(0) 
            # cv2.destroyAllWindows()
            
            #load cascade classifier training file for haarcascade 
            #haar_face_cascade = cv2.CascadeClassifier('C:/Users/sarah/Documents/Python_Scripts/dev_folder/face_detection/haarcascade_frontalface_default.xml')
       #     try:
        #        cascPath = 'haarcascade_frontalface_alt.xml'
         #       logging.info('successfully loaded trained Haar cascade')
          #  except:
           #     logging.error('could not find xml for Haar cascade')
          #  cascPath ='C:/Users/sarah/AppData/Local/Continuum/anaconda2/pkgs/opencv/sources/data/haarcascades/haarcascade_frontalface_alt.xml'
       #     cascPath ='C:/Users/sarah/AppData/Local/Continuum/anaconda2/pkgs/opencv/sources/data/haarcascades/haarcascade_fullbody.xml'
            
           # faceCascade = cv2.CascadeClassifier(cascPath)
            try:
                gray_img = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)
            
                faces = faceCascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=2,  minSize=(30, 30));  
            
            #print the number of faces found 
                print('Faces found: ', len(faces))
                logging.info('found %s faces', len(faces))
            #go over list of faces and draw them as rectangles on original colored 
            
            #generate a green box for the faces
        #      for (x, y, w, h) in faces:     
       #         cv2.rectangle(test1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            #convert image to RGB and show image 
   #         plt.savefig(os.path.join('processed_images', test1))
         #   plt.imshow(convertToRGB(test1))
        #    plt.show()
         #cvtColor( image, gray_image, COLOR_BGR2GRAY );
                file_name = os.path.join('face_detection', file)
    
                if len(faces)>0:
                    
                    try:
                        cv2.imwrite(file_name, test1);
                        logging.info('saved processed image at %s', file)
                    except:
                        logging.error('could not save file %s', file)
                        logging.error('current working directory: %s', os.getcwd())
              #      namedWindow( imageName, WINDOW_AUTOSIZE );
               #     namedWindow( "Gray image", WINDOW_AUTOSIZE );
    
                else:
                    logging.info('No faces found in %s', file)
            except: 
                logging.info('error opening file: %s', file)
            #    file_name = os.path.join('exception_files', file)
             #   shutil.move(file_name, file)   
                    
        elif file.endswith('png'):
            try:
                gray_img = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)
            
                faces = faceCascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=2,  minSize=(30, 30));  
            
            #print the number of faces found 
                print('Faces found: ', len(faces))
                logging.info('found %s faces', len(faces))
            #go over list of faces and draw them as rectangles on original colored 
            
            #generate a green box for the faces
        #      for (x, y, w, h) in faces:     
       #         cv2.rectangle(test1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            #convert image to RGB and show image 
   #         plt.savefig(os.path.join('processed_images', test1))
         #   plt.imshow(convertToRGB(test1))
        #    plt.show()
         #cvtColor( image, gray_image, COLOR_BGR2GRAY );
                file_name = os.path.join('face_detection', file)
    
                if len(faces)>0:
                    
                    try:
                        cv2.imwrite(file_name, test1);
                        logging.info('saved processed image at %s', file)
                    except:
                        logging.error('could not save file %s', file)
                        logging.error('current working directory: %s', os.getcwd())
              #      namedWindow( imageName, WINDOW_AUTOSIZE );
               #     namedWindow( "Gray image", WINDOW_AUTOSIZE );
    
                else:
                    logging.info('No faces found in %s', file)
            except: 
                logging.info('error opening file: %s', file)
          #      file_name = os.path.join('exception_files', file)
           #     shutil.move(file_name, file)   
                    
                
        else:
            print('not an image file')
            
main()