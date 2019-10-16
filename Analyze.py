
import csv
from scipy.io import wavfile 
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as scst
import os

#fs,data=wavfile.read('HandheldRecorded/BeatExtracted/cw_anirudh_358_beat.wav')
#%%


def ExtractFreq(data):
    Pxx, freqs, times, im = plt.specgram(data,Fs=fs)
    
        
    intervals = len(times);
    block = np.int(np.ceil(intervals/4))
    ti1 = np.sum(Pxx[:,0:block-1], axis = 1);
    ti2 = np.sum(Pxx[:,block:2*block-1], axis = 1)
    ti3 = np.sum(Pxx[:,2*block:3*block-1], axis = 1)
    ti4 = np.sum(Pxx[:,3*block:intervals-1], axis = 1)
    
    
    #%%
    
    Freq_vals = []
    cumsum1= np.cumsum(ti1)
    cumsum1 = cumsum1/max(cumsum1)

    flag1=0
    flag2=0
    flag3=0
    for i in range(int(len(cumsum1))):
        if(cumsum1[i]>0.95 and flag3==0):
            if(abs(cumsum1[i]-0.95)<abs(cumsum1[i-1]-0.95)):
                percent95_1=freqs[i]
            else:
                percent95_1 = freqs[i-1]
            flag3=1
        if(cumsum1[i]>0.5 and flag1==0):
            if(abs(cumsum1[i]-0.5)<abs(cumsum1[i-1]-0.5)):
                percent50_1=freqs[i]
            else:
                percent50_1 = freqs[i-1]
            flag1=1
        if(cumsum1[i]>0.05 and flag2==0):
            if(abs(cumsum1[i]-0.05)<abs(cumsum1[i-1]-0.05)):
                percent5_1=freqs[i]
            else:
                percent5_1 = freqs[i-1]
            flag2=1;
    
    Freq_vals.append(percent95_1)
    Freq_vals.append(percent50_1)
    Freq_vals.append(percent5_1)


    #%%
    cumsum2= np.cumsum(ti2)
    cumsum2 = cumsum2/max(cumsum2)
    
    flag1=0
    flag2=0
    flag3=0
    for i in range(int(len(cumsum2))):
        if(cumsum2[i]>0.95 and flag3==0):
            if(abs(cumsum2[i]-0.95)<abs(cumsum2[i-1]-0.95)):
                percent95_2=freqs[i]
            else:
                percent95_2 = freqs[i-1]
            flag3=1
        if(cumsum2[i]>0.5 and flag1==0):
            if(abs(cumsum2[i]-0.5)<abs(cumsum2[i-1]-0.5)):
                percent50_2=freqs[i]
            else:
                percent50_2 = freqs[i-1]
            flag1=1
        if(cumsum2[i]>0.05 and flag2==0):
            if(abs(cumsum2[i]-0.05)<abs(cumsum2[i-1]-0.05)):
                percent5_2=freqs[i]
            else:
                percent5_2 = freqs[i-1]
            flag2=1;
 
    Freq_vals.append(percent95_2)
    Freq_vals.append(percent50_2)
    Freq_vals.append(percent5_2) 
    #%%
    cumsum3= np.cumsum(ti3)
    cumsum3 = cumsum3/max(cumsum3)
    
    flag1=0
    flag2=0
    flag3=0
    for i in range(int(len(cumsum3))):
        if(cumsum3[i]>0.95 and flag3==0):
            if(abs(cumsum3[i]-0.95)<abs(cumsum3[i-1]-0.95)):
                percent95_3=freqs[i]
            else:
                percent95_3 = freqs[i-1]
            flag3=1
        if(cumsum3[i]>0.5 and flag1==0):
            if(abs(cumsum3[i]-0.5)<abs(cumsum3[i-1]-0.5)):
                percent50_3=freqs[i]
            else:
                percent50_3 = freqs[i-1]
            flag1=1
        if(cumsum3[i]>0.05 and flag2==0):
            if(abs(cumsum3[i]-0.05)<abs(cumsum3[i-1]-0.05)):
                percent5_3=freqs[i]
            else:
                percent5_3 = freqs[i-1]
            flag2=1;
    Freq_vals.append(percent95_3)
    Freq_vals.append(percent50_3)
    Freq_vals.append(percent5_3)
    
    #%%
    cumsum4= np.cumsum(ti4)
    cumsum4 = cumsum4/max(cumsum4)
    
    #print(cumsum4)
    #print(freqs)
    flag1=0
    flag2=0
    flag3=0
    for i in range(int(len(cumsum4))):
        if(cumsum4[i]>0.95 and flag3==0):
            if(abs(cumsum4[i]-0.95)<abs(cumsum4[i-1]-0.95)):
                percent95_4=freqs[i]
            else:
                percent95_4 = freqs[i-1]
            flag3=1
        if(cumsum4[i]>0.5 and flag1==0):
            if(abs(cumsum4[i]-0.5)<abs(cumsum4[i-1]-0.5)):
                percent50_4=freqs[i]
            else:
                percent50_4 = freqs[i-1]
            flag1=1
            #print(percent50_4)
        if(cumsum4[i]>0.05 and flag2==0):
            if(abs(cumsum4[i]-0.05)<abs(cumsum4[i-1]-0.05)):
                percent5_4=freqs[i]
            else:
                percent5_4 = freqs[i-1]
            #print(percent5_4)
            flag2=1;
    Freq_vals.append(percent95_4)
    Freq_vals.append(percent50_4)
    Freq_vals.append(percent5_4)
    
    return Freq_vals

#%%
#freqparams=ExtractFreq(data)
#%%

files=os.listdir('HandheldRecorded/BeatExtracted')      
files.sort()
with open('DataNewParams.csv', mode='w') as datafile: 
    datafile_writer = csv.writer(datafile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for file in files:
        file_path = "HandheldRecorded/BeatExtracted/"+file
        fs, beat = wavfile.read(file_path)
        freqparam=ExtractFreq(beat)
        datafile_writer.writerow([file, freqparam[0], freqparam[1], freqparam[2], freqparam[3], freqparam[4], freqparam[5], freqparam[6], freqparam[7], freqparam[8], freqparam[9], freqparam[10], freqparam[11]])
    
        
        
#fs,data=wavfile.read("HandheldRecorded/BeatExtracted/cw_ranjith_3_48_beat.wav")
#freqparams=ExtractFreq(data)
