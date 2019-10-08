
from scipy.io import wavfile
fs, data = wavfile.read('cw_adiveppa_4_19.wav')
import matplotlib.pyplot as plt
import numpy as np


def analyze(data,x,y,fs):
    beat=data[x:y]
    Pxx, freqs, times, im = plt.specgram(beat, NFFT=1024, Fs=fs,noverlap=256)
    plt.show()
    Pxx=10*np.log10(Pxx)
    freq=np.zeros((len(freqs),len(times)))
    max_array=np.zeros(len(times))
    min_array=np.zeros(len(times))
    range_array=np.zeros(len(times))
    mean_array=np.zeros(len(times))
    temp=np.zeros(len(freq))
    stat_max=np.zeros(2)
    stat_min=np.zeros(2)
    stat_range=np.zeros(2)
    stat_mean=np.zeros(2)
    for j in range(len(times)):
        for i in range(len(freqs)):
            if(Pxx[i][j]>=30):
                freq[i][j]=freqs[i]
        max_array[j]=max(freq[:,j])
        temp=freq[:,j]
        temp=temp[np.nonzero(temp)]
        min_array[j]=min(temp)
        range_array[j]=max_array[j]-min_array[j]
        mean_array[j]=np.mean(temp)
    stat_max[0]=max(max_array[0:2])
    stat_max[1]=max(max_array[2:])
    stat_min[0]=min(min_array[0:2])
    stat_min[1]=min(min_array[2:])
    stat_range=stat_max-stat_min
    stat_mean[0]=np.mean(mean_array[0:2])
    stat_mean[1]=np.mean(mean_array[2:])
    return stat_max,stat_min,stat_range,stat_mean
a,b,c,d=analyze(data,72860,76740,fs)