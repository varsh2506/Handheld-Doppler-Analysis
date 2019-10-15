
from scipy.io import wavfile
fs, data = wavfile.read('HandheldRecorded\\cw_ajay_1_17_beat.wav')
import matplotlib.pyplot as plt
import numpy as np


beat=data;
seglength = len(beat)/4;
windowa = np.ones(np.int(len(beat)/4));
Pxx, freqs, times, im = plt.specgram(beat,Fs=fs)

intervals = len(times);
block = np.int(np.ceil(intervals/4));
ti1 = np.zeros(int(len(Pxx)))
ti2 = np.zeros(int(len(Pxx)))
ti3 = np.zeros(int(len(Pxx)))
ti4 = np.zeros(int(len(Pxx)))
ti1 = np.sum(Pxx[:,0:block-1], axis = 1);
ti2 = np.sum(Pxx[:,block:2*block-1], axis = 1)
ti3 = np.sum(Pxx[:,2*block:3*block-1], axis = 1)
ti4 = np.sum(Pxx[:,3*block:intervals-1], axis = 1)


#%%
print(Pxx[:,0:12])


#%%

plt.show()
#    Pxx=10*np.log10(Pxx)
#    freq=np.zeros((len(freqs),len(times)))
#    max_array=np.zeros(len(times))
#    min_array=np.zeros(len(times))
#    range_array=np.zeros(len(times))
#    mean_array=np.zeros(len(times))
#    temp=np.zeros(len(freq))
#    stat_max=np.zeros(2)
#    stat_min=np.zeros(2)
#    stat_range=np.zeros(2)
#    stat_mean=np.zeros(2)
#    for j in range(len(times)):
#        for i in range(len(freqs)):
#            if(Pxx[i][j]>=30):
#                freq[i][j]=freqs[i]
#        max_array[j]=max(freq[:,j])
#        temp=freq[:,j]
#        temp=temp[np.nonzero(temp)]
#        min_array[j]=min(temp)
#        range_array[j]=max_array[j]-min_array[j]
#        mean_array[j]=np.mean(temp)
#    stat_max[0]=max(max_array[0:2])
#    stat_max[1]=max(max_array[2:])
#    stat_min[0]=min(min_array[0:2])
#    stat_min[1]=min(min_array[2:])
#    stat_range=stat_max-stat_min
#    stat_mean[0]=np.mean(mean_array[0:2])
#    stat_mean[1]=np.mean(mean_array[2:]

#%%
print(len(TI1))
cumsum1= np.cumsum(ti1)
cumsum1 = cumsum1/max(cumsum1)
flag1=0
flag2=0
for i in range(int(len(cumsum1))):
    if(cumsum1[i]>0.95):
        percent95_1 = freqs[i]
        break
    elif(cumsum1[i]>0.5 and flag1==0):
        percent50_1 = freqs[i]
        flag1=1
    elif(cumsum1[i]>0.05 and flag2==0):
        percent5_1=freqs[i]
        flag2=1;
print(percent95_1)
print(percent50_1)
print(percent5_1)

#%%
cumsum2= np.cumsum(ti2)
cumsum2 = cumsum2/max(cumsum2)
flag1=0
flag2=0
for i in range(int(len(cumsum2))):
    if(cumsum2[i]>0.95):
        percent95_2 = freqs[i]
        break
    elif(cumsum2[i]>0.5 and flag1==0):
        percent50_2 = freqs[i]
        flag1=1
    elif(cumsum2[i]>0.05 and flag2==0):
        percent5_2=freqs[i]
        flag2=1;
print(percent95_2)
print(percent50_2)
print(percent5_2)
#%%
cumsum3= np.cumsum(ti3)
cumsum3 = cumsum3/max(cumsum3)
flag1=0
flag2=0
for i in range(int(len(cumsum3))):
    if(cumsum3[i]>0.95):
        percent95_3 = freqs[i]
        break
    elif(cumsum3[i]>0.5 and flag1==0):
        percent50_3 = freqs[i]
        flag1=1
    elif(cumsum3[i]>0.05 and flag2==0):
        percent5_3=freqs[i]
        flag2=1;
print(percent95_3)
print(percent50_3)
print(percent5_3)
#%%
cumsum4= np.cumsum(ti4)
cumsum4 = cumsum4/max(cumsum4)
flag1=0
flag2=0
for i in range(int(len(cumsum4))):
    if(cumsum4[i]>0.95):
        percent95_4 = freqs[i]
        break
    elif(cumsum4[i]>0.5 and flag1==0):
        percent50_4 = freqs[i]
        flag1=1
    elif(cumsum4[i]>0.05 and flag2==0):
        percent5_4=freqs[i]
        flag2=1;
print(percent95_4)
print(percent50_4)
print(percent5_4)