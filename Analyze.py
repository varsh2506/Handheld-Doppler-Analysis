
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
TI1 = np.sum(Pxx[0:block-1,:], axis = 1);
TI2 = np.sum(Pxx[block:2*block-1,:], axis = 1)
TI3 = np.sum(Pxx[2*block:3*block-1,:], axis = 1)
TI4 = np.sum(Pxx[3*block:intervals-1,:], axis = 1)


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
