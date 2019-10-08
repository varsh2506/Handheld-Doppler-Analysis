# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 16:58:36 2019

@author: Mehak
"""

#%%
import csv
from scipy.io import wavfile 
import matplotlib.pyplot as plt
#%%

with open('Data.csv', 'r') as f:
    reader = csv.reader(f)
    all_files = list(reader)


#%%

no_of_records = len(all_files)

for i in range(1,no_of_records):
    #Extracting each record
    record = all_files[i]
    #Getting the file name from each record extracted (first column)
    file = record[0]
    file_name = file + '.wav'
    file_path = 'HandheldRecorded\\' + file_name
    #Reading corresponding file  
    fs, audio_file =  wavfile.read(file_path)

plt.plot(audio_file)


