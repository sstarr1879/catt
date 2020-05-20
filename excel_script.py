# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 09:06:08 2018

@author: sarah
"""

import urllib.request
import xlsxwriter
import os
import sys


dir_wanted = os.chdir(os.path.dirname(sys.argv[0]))
#uncomment the following line if you don't want the current directory
#dir_wanted = "C:\\users\\doe_j"


file_list = [file for file in os.listdir(dir_wanted) if file.endswith('.png') or file.endswith('.jpg')]
full_path_list = [dir_wanted + '\\' + file for file in file_list]

name_list = []
num_list = []

for item in file_list:
    temp_list = item.rpartition('_')
    name = str(temp_list[0])
    num = str(temp_list[2].rpartition('.')[0])
    name_list.append(name)
    num_list.append(num)

#%%
workbook = xlsxwriter.Workbook('pics_and_links.xlsx')
ws = workbook.add_worksheet('Links')

#adding column titles and making them bold
bold = workbook.add_format({'bold': True})
ws.write('A1', "Name", bold)
ws.write('B1', "Number", bold)
ws.write('C1', "Link", bold)

#putting the three lists we made into the workbook
for i in range (0, len(full_path_list)):
    row_num = i + 2
    ws.write('A%d' % row_num, name_list[i])
    ws.write('B%d' % row_num, int(num_list[i]))
    ws.write_url('C%d' % row_num, full_path_list[i])

#Set the width of the column with the links in it
ws.set_column(2, 2, 40)

workbook.close()