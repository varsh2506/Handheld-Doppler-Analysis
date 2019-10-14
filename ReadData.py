# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 16:58:36 2019

@author: Mehak
"""

#%%
import csv
from scipy.io import wavfile 
import matplotlib.pyplot as plt
import numpy as np
import os
import scipy.stats as scst

#%%

with open('Data.csv', 'r') as f:
    reader = csv.reader(f)
    all_files = list(reader)

#%%

def analyze(data,beat_start,beat_end,fs):
    
    beat=data[beat_start:beat_end]
    Pxx, freqs, times, im = plt.specgram(beat, NFFT=1024, Fs=fs,noverlap=256)
    plt.show()
    
    Pxx=10*np.log10(Pxx)
    freqmax=np.zeros((len(freqs),len(times)))
    freqmin=np.zeros((len(freqs),len(times)))

    
    max_array=np.zeros(len(times))
    min_array=np.multiply(np.ones(len(times)),22050)
    range_array=np.zeros(len(times))
    mean_array=np.zeros(len(times))
    
    temp=np.zeros(len(freqs))
  
    
    for j in range(len(times)):
        for i in range(len(freqs)):
            if(Pxx[i][j]>=30):
                freqmax[i][j]=freqs[i]
            elif(Pxx[i][j]>=0):
                freqmin[i][j]= freqs[i]
            
        max_array[j]=max(freqmax[:,j])
        temp=freqmin[:,j]
        temp = temp[np.nonzero(temp)]
        if(len(temp) == 0):
            min_array[j] = 22050
            mean_array[j]= 0
        else:
            min_array[j]=min(temp)
            mean_array[j]=np.mean(temp)        
        
    stat_max=max(max_array)
    stat_min=min(min_array)
    stat_range=stat_max-stat_min
    stat_mean=np.mean(mean_array)
    
    return stat_max,stat_min,stat_range,stat_mean


#%%

def index_value(fs,data):
    window_size = 0.2*fs
    beat = []
    time_interval = [0, 0] #Start and end of the beat in terms of seconds
    #print(len(data))
    #print(window_size)
    #print ("Number of windows: ", int((len(data))/window_size))
    ct = 0
    avg=np.zeros(int((len(data))/window_size))
    for i in range(0, int((len(data))/window_size)-1):    
        frame = data[int(np.ceil(i*window_size)):int(np.ceil((i+1)*window_size))]
        avg[i] = np.mean(np.absolute(frame)) #Computing the average of the signal in each window frame
     #   print ("Average", avg[i])
    #print(max(avg))
    #print(np.mean(avg))
    dynamic_threshold=np.mean(avg)
    #print(dynamic_threshold)
    for i in range(0, int((len(data))/window_size)-1):       
        if avg[i]>=dynamic_threshold: #Manually set threshold after observation (might have to be changed)
     #       print(i)
            if beat==[]:
                time_interval[0] = (i*window_size)
            for sample in frame:
                beat.append(sample)
        elif beat!=[]: #Extracting the second beat
            ct+=1
            if ct==1:
                beat = []
            else:
                time_interval[1] = (i*window_size)
                break
    return int(time_interval[0]),int(time_interval[1])



#%%

no_of_records = len(all_files)

for i in range(0,no_of_records):
    #Extracting each record
    record = all_files[i]
    #Getting the file name from each record extracted (first column)
    file = record[0]
    file_name = file + '.wav'
    file_path = 'HandheldRecorded\\' + file_name
    #Reading corresponding file  
    fs, audio_file =  wavfile.read(file_path)
    beat_start, beat_end = index_value(fs,audio_file)
    maxf, minf, rangef,meanf = analyze(audio_file, beat_start, beat_end, fs)
    energy = sum(np.power(np.asarray(audio_file[beat_start:beat_end]),2))
    record.extend([maxf,minf,rangef,meanf,energy])

#%%
with open("DataWithParams.csv", "w", newline ='') as f:
    writer = csv.writer(f)
    writer.writerows(all_files)

#%%

with open("DataWithParams.csv","r") as f:
    csvreader = csv.reader(f)
    all_records = list(csvreader)

maxf_array = []
meanf_array = []
rangef_array = []
psv_array = []
diameter_array = []
depth_array = []
energy_array = []

for i in range(len(all_records)):
    record = all_records[i]
    maxf_array.append(record[4])
    meanf_array.append(record[6])
    rangef_array.append(record[7])
    energy_array.append(record[8])
    psv_array.append(record[1])
    diameter_array.append(record[3])
    depth_array.append(record[2])

#%%
psv_array = np.asarray([float(i) for i in psv_array], dtype = np.float32)
diameter_array = np.asarray([float(i) for i in diameter_array], dtype = np.float32)
depth_array = np.asarray([float(i) for i in depth_array], dtype = np.float32)
maxf_array = np.asarray([float(i) for i in maxf_array], dtype = np.float32)
meanf_array = np.asarray([float(i) for i in meanf_array], dtype = np.float32)
rangef_array = np.asarray([float(i) for i in rangef_array], dtype = np.float32)
volume_array = np.multiply(psv_array,diameter_array)   
energy_array = np.asarray([float(i) for i in energy_array], dtype = np.float32) 
    
#%%

#Correlation between max frequency and psv --- 1 

covariance_1 = np.cov(maxf_array,psv_array)
corr1, _ = scst.pearsonr(maxf_array,psv_array)
corrs1,v = scst.spearmanr(maxf_array,psv_array)
print(covariance_1[0][1])
print(corr1)
print(corrs1)

#%%
#Correlation between max frequency and diameter --- 2

covariance_2 = np.cov(maxf_array,diameter_array)
corr2, _ = scst.pearsonr(maxf_array,diameter_array)
corrs2,v = scst.spearmanr(maxf_array,diameter_array)
print(covariance_2[0][1])
print(corr2)
print(corrs2)
    
#%%

#Correlation between max frequency and depth --- 3

covariance_3 = np.cov(maxf_array,depth_array)
corr3, _ = scst.pearsonr(maxf_array,depth_array)
corrs3,v = scst.spearmanr(maxf_array,depth_array)
print(covariance_3[0][1])
print(corr3)
print(corrs3)

#%%

#Correlation between max frequency and volume --- 4 

covariance_4 = np.cov(maxf_array,volume_array)
corr4, _ = scst.pearsonr(maxf_array,volume_array)
corrs4,v = scst.spearmanr(maxf_array,volume_array)
print(covariance_4[0][1])
print(corr4)
print(corrs4)

#%%
#Correlation between mean of frequency and psv --- 5 

covariance_5 = np.cov(meanf_array,psv_array)
corr5, _ = scst.pearsonr(meanf_array,psv_array)
corrs5,v = scst.spearmanr(meanf_array,psv_array)
print(covariance_5[0][1])
print(corr5)
print(corrs5)

#%%

#Correlation between mean of frequency and diameter --- 6

covariance_6 = np.cov(meanf_array,diameter_array)
corr6, _ = scst.pearsonr(meanf_array,diameter_array)
corrs6,v = scst.spearmanr(meanf_array,diameter_array)
print(covariance_6[0][1])
print(corr6)
print(corrs6)

#%%

#Correlation between mean of frequency and depth --- 7

covariance_7 = np.cov(meanf_array,depth_array)
corr7, _ = scst.pearsonr(meanf_array,depth_array)
corrs7,v = scst.spearmanr(meanf_array,depth_array)
print(covariance_7[0][1])
print(corr7)
print(corrs7)

#%%

#Correlation between mean of frequency and volume

covariance_8 = np.cov(meanf_array,volume_array)
corr8, _ = scst.pearsonr(meanf_array,volume_array)
corrs8,v = scst.spearmanr(meanf_array,volume_array)
print(covariance_8[0][1])
print(corr8)
print(corrs8)

#%%

covariance_9 = np.cov(energy_array,psv_array)
corr9, _ = scst.pearsonr(energy_array,psv_array)
corrs9,v = scst.spearmanr(energy_array,psv_array)
print(covariance_9[0][1])
print(corr9)
print(corrs9)

#%%

covariance_10 = np.cov(energy_array,diameter_array)
corr10, _ = scst.pearsonr(energy_array,diameter_array)
corrs10,v = scst.spearmanr(energy_array,diameter_array)
print(covariance_10[0][1])
print(corr10)
print(corrs10)

#%%

covariance_11 = np.cov(energy_array,depth_array)
corr11, _ = scst.pearsonr(energy_array,depth_array)
corrs11,v = scst.spearmanr(energy_array,depth_array)
print(covariance_11[0][1])
print(corr11)
print(corrs11)

#%%

covariance_12 = np.cov(energy_array,volume_array)
corr12, _ = scst.pearsonr(energy_array,volume_array)
corrs12,v = scst.spearmanr(energy_array,volume_array)
print(covariance_12[0][1])
print(corr12)
print(corrs12)
