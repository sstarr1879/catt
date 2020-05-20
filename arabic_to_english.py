"""
Created on Wed Aug 22 12:19:11 2018

@author: sarah
"""

from unidecode import unidecode
import os
#%%

#check that the function works
print(unidecode(u"۰۱۲۳۴۵۶۷۸۹"))
#%%
#run through the filenames and convert them
for filename in os.listdir("."):
    if filename.contains("cheese_"):
        os.rename(filename, unidecode(u'filename')



