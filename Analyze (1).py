
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
    return max_array,min_array,range_array,mean_array
x,y,z,w=analyze(data,72860,76740,fs)