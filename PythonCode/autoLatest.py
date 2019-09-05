import scipy.io.wavfile as wav
from scipy import signal
import numpy as np
import peakutils
import scipy.signal as signal
from matplotlib import pyplot as plot
import matplotlib.mlab as mlab
import math
from statistics import mean,median

def autocorr(x,lags):
    corr=[1. if l==0 else np.corrcoef(x[l:],x[:-l])[0][1] for l in range(0,lags)]
    return np.array(corr)


fs, data = wav.read('150328_0427.wav')
#fs2, data1 = wav.read('150328_0427_mono.wav')

#wiener_output = signal.wiener(data,mysize=2205)

sampleRate = int(fs)
print(sampleRate)
overlap = int(np.ceil(sampleRate*0.015))

time = 0.02
interval = 2.5
numWindowsNeeded =  int(interval/time)
numFramesNeeded = int(math.ceil(time * sampleRate))
totalWindows = math.floor(len(data)/numFramesNeeded)
numVelocitySamples = math.ceil(totalWindows/numWindowsNeeded) - 1;

velocityArray = []

#for i in range(0,numVelocitySamples-1):
	##Take a part of the complete signal
	#signalArray = data[i*(numWindowsNeeded+2)*numFramesNeeded:(i+1)*(numWindowsNeeded+2)*numFramesNeeded]
	
	##Find Mean
	#meanArray = []
	#for j in range(0,numWindowsNeeded):
		#meanArray.append(mean(np.absolute(signalArray[j*numFramesNeeded:(j+1)*numFramesNeeded])))
	#threshold = mean(meanArray)
	
	##Find Minimum Frame
	#peakArray = []
	
	#for j in range(0,numWindowsNeeded):
		#if(meanArray[j]>threshold):
			#autoCorrelationArray = autocorr(np.array(signalArray[j*numFramesNeeded:(j+1)*numFramesNeeded]),500)
			#plot.plot(autoCorrelationArray)
			#peakind = signal.find_peaks(autoCorrelationArray, distance=10)
			#peakArray.append(peakind[0][0])
		#else:
			#peakArray.append(500)
	#plot.show()	
	
	##print(peakind)
	#minPeak = min(peakArray)
	
	#velocity = ((44100 / minPeak)* 1540.0)/80000.0
	#velocityArray.append(velocity)
	
	
fs = 44100 # sample rate 
f = 600 # the frequency of the signal

x = np.arange(fs) # the points on the x axis for plotting
# compute the value (amplitude) of the sin wave at the for each sample
y = np.sin(2*np.pi*f * (x/fs)) 

#this instruction can only be used with IPython Notbook. 

# showing the exact location of the smaples
z = autocorr(y,1000)

plot.clf()
plot.plot(y)
#plot.subplot(211)
#plot.plot(data)

#plot.ylim([0,3000])
#plot.subplot(212)
#plot.specgram(x=data1,NFFT=numFramesNeeded,  Fs=sampleRate, noverlap=overlap)
#plot.ylim([0,3000])

plot.show()

#print(median(velocityArray))




