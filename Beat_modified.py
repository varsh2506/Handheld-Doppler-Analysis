#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 21:21:13 2019

@author: kshama
"""

from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
import os

fs,data=wavfile.read('cw_saurav_5_04.wav')
plt.figure(1)
plt.title('Plot audio file')
plt.plot(data)
plt.show()
def index_value(fs,data):
    window_size = 0.2*fs
    beat = []
    time_interval = [0, 0] #Start and end of the beat in terms of seconds
    print(len(data))
    print(window_size)
    print ("Number of windows: ", int((len(data))/window_size))
    ct = 0
    avg=np.zeros(int((len(data))/window_size))
    for i in range(0, int((len(data))/window_size)-1):    
        frame = data[int(np.ceil(i*window_size)):int(np.ceil((i+1)*window_size))]
        avg[i] = np.mean(np.absolute(frame)) #Computing the average of the signal in each window frame
        print ("Average", avg[i])
    print(max(avg))
    print(np.mean(avg))
    dynamic_threshold=max(avg)-np.mean(avg)
    print(dynamic_threshold)
    for i in range(0, int((len(data))/window_size)-1):       
        if avg[i]>=dynamic_threshold: #Manually set threshold after observation (might have to be changed)
            print(i)
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
    return time_interval[0],time_interval[1]

