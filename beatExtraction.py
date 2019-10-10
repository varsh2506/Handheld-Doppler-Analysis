#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:45:55 2019

@author: varshini
"""

import matplotlib.pyplot as plt
import numpy as np
import wave

spf = wave.open('cw_ranjith_3_45.wav','r')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')
fs = spf.getframerate()

Time=np.linspace(0, len(signal)/fs, num=len(signal))


#Plot the audio signal in time domain
plt.figure(1)
plt.title('Plot in time domain')
plt.plot(Time,signal)
plt.show()

window_size = 0.005
beat = []
time_interval = [0, 0] #Start and end of the beat in terms of seconds
print ("Number of windows: ", int((len(signal)/fs)/window_size))
ct = 0
for i in range(0, int((len(signal)/fs)/window_size)-1):    
    frame = signal[int(np.ceil(i*fs*window_size)):int(np.ceil((i+1)*fs*window_size))]
    avg = np.mean(np.absolute(frame)) #Computing the average of the signal in each window frame
    print ("Average", avg)
    if avg>=250: #Manually set threshold after observation (might have to be changed)
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
  

print (time_interval[1], time_interval[0])
Time = np.linspace(time_interval[0], time_interval[1], (time_interval[1]-time_interval[0])*fs)  
plt.figure(2)
plt.title('Beat')
plt.plot(Time,beat)
plt.show()
    