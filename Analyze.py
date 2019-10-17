
import csv
from scipy.io import wavfile
from scipy import signal 
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as scst
import os

#fs,data=wavfile.read('HandheldRecorded/BeatExtracted/cw_anirudh_358_beat.wav')
#%%


def ExtractFreq(data,fs):
    #data=signal.resample(data,8000)
    Pxx, freqs, times, im = plt.specgram(data,Fs=fs)
    fmax=8000
    freq_slice = np.where((freqs <= fmax))

    # keep only frequencies of interest
    freqs   = freqs[freq_slice]
    Pxx = Pxx[freq_slice,:][0]
        
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
        freqparam=ExtractFreq(beat,fs)
        datafile_writer.writerow([file, freqparam[0], freqparam[1], freqparam[2], freqparam[3], freqparam[4], freqparam[5], freqparam[6], freqparam[7], freqparam[8], freqparam[9], freqparam[10], freqparam[11]])
        
        
        
'''#fs,data=wavfile.read("HandheldRecorded/BeatExtracted/cw_ranjith_3_48_beat.wav")
#freqparams=ExtractFreq(data)
with open("DataNewParams.csv",mode="r") as f:
    csvreader = csv.reader(f)
    all_records = list(csvreader)
maxf1_array = []
maxf2_array = []
maxf3_array = []
maxf4_array = []
meanf1_array = []
meanf2_array = []
meanf3_array = []
meanf4_array = []
psv_array = []
diameter_array = []
depth_array = []

for i in range(len(all_records)):
    record = all_records[i]
    
    maxf1_array.append(record[1])
    maxf2_array.append(record[4])  
    maxf3_array.append(record[7])
    maxf4_array.append(record[10])  
    meanf1_array.append(record[2])
    meanf2_array.append(record[5])
    meanf3_array.append(record[8])
    meanf4_array.append(record[11])
    psv_array.append(record[13])
    diameter_array.append(record[15])
    depth_array.append(record[14])
#%%
psv_array = np.asarray([float(i) for i in psv_array], dtype = np.float32)
diameter_array = np.asarray([float(i) for i in diameter_array], dtype = np.float32)
depth_array = np.asarray([float(i) for i in depth_array], dtype = np.float32)
maxf1_array = np.asarray([float(i) for i in maxf1_array], dtype = np.float32)
meanf1_array = np.asarray([float(i) for i in meanf1_array], dtype = np.float32)
maxf2_array = np.asarray([float(i) for i in maxf1_array], dtype = np.float32)
meanf2_array = np.asarray([float(i) for i in meanf1_array], dtype = np.float32)
maxf3_array = np.asarray([float(i) for i in maxf1_array], dtype = np.float32)
meanf3_array = np.asarray([float(i) for i in meanf1_array], dtype = np.float32)
maxf4_array = np.asarray([float(i) for i in maxf1_array], dtype = np.float32)
meanf4_array = np.asarray([float(i) for i in meanf1_array], dtype = np.float32)
volume_array = np.multiply(psv_array,diameter_array)

plt.stem(psv_array,maxf2_array) 
plt.show()  

#%%
covariance_1 = np.cov(maxf1_array,psv_array)
corr1, _ = scst.pearsonr(maxf1_array,psv_array)
corrs1,v = scst.spearmanr(maxf1_array,psv_array)
print(covariance_1[0][1])
print(corr1)
print(corrs1)

#%%
covariance_2 = np.cov(meanf1_array,psv_array)
corr2, _ = scst.pearsonr(meanf1_array,psv_array)
corrs2,v = scst.spearmanr(meanf1_array,psv_array)
print(covariance_2[0][1])
print(corr2)
print(corrs2)

#%%
covariance_3 = np.cov(maxf1_array,diameter_array)
corr3, _ = scst.pearsonr(maxf1_array,diameter_array)
corrs3,v = scst.spearmanr(maxf1_array,diameter_array)
print(covariance_3[0][1])
print(corr3)
print(corrs3)

#%%
covariance_4 = np.cov(meanf1_array,diameter_array)
corr4, _ = scst.pearsonr(meanf1_array,diameter_array)
corrs4,v = scst.spearmanr(meanf1_array,diameter_array)
print(covariance_4[0][1])
print(corr4)
print(corrs4)

#%%
covariance_5 = np.cov(maxf1_array,depth_array)
corr5, _ = scst.pearsonr(maxf1_array,depth_array)
corrs5,v = scst.spearmanr(maxf1_array,depth_array)
print(covariance_5[0][1])
print(corr5)
print(corrs5)

#%%
covariance_6 = np.cov(meanf1_array,depth_array)
corr6, _ = scst.pearsonr(meanf1_array,depth_array)
corrs6,v = scst.spearmanr(meanf1_array,depth_array)
print(covariance_6[0][1])
print(corr6)
print(corrs6)

#%%
covariance_7 = np.cov(maxf2_array,psv_array)
corr7, _ = scst.pearsonr(maxf2_array,psv_array)
corrs7,v = scst.spearmanr(maxf2_array,psv_array)
print(covariance_7[0][1])
print(corr7)
print(corrs7)

#%%
covariance_8 = np.cov(meanf2_array,psv_array)
corr8, _ = scst.pearsonr(meanf2_array,psv_array)
corrs8,v = scst.spearmanr(meanf2_array,psv_array)
print(covariance_8[0][1])
print(corr8)
print(corrs8)

#%%
covariance_9 = np.cov(maxf2_array,diameter_array)
corr9, _ = scst.pearsonr(maxf2_array,diameter_array)
corrs9,v = scst.spearmanr(maxf2_array,diameter_array)
print(covariance_9[0][1])
print(corr9)
print(corrs9)

#%%
covariance_10 = np.cov(meanf2_array,diameter_array)
corr10, _ = scst.pearsonr(meanf2_array,diameter_array)
corrs10,v = scst.spearmanr(meanf2_array,diameter_array)
print(covariance_10[0][1])
print(corr10)
print(corrs10)

#%%
covariance_11 = np.cov(maxf2_array,depth_array)
corr11, _ = scst.pearsonr(maxf2_array,depth_array)
corrs11,v = scst.spearmanr(maxf2_array,depth_array)
print(covariance_11[0][1])
print(corr11)
print(corrs11)

#%%
covariance_12 = np.cov(meanf2_array,depth_array)
corr12, _ = scst.pearsonr(meanf2_array,depth_array)
corrs12,v = scst.spearmanr(meanf2_array,depth_array)
print(covariance_12[0][1])
print(corr12)
print(corrs12)
#%%
#%%
covariance_13 = np.cov(maxf3_array,psv_array)
corr13, _ = scst.pearsonr(maxf3_array,psv_array)
corrs13,v = scst.spearmanr(maxf3_array,psv_array)
print(covariance_13[0][1])
print(corr13)
print(corrs13)

#%%
covariance_14 = np.cov(meanf3_array,psv_array)
corr14, _ = scst.pearsonr(meanf3_array,psv_array)
corrs14,v = scst.spearmanr(meanf3_array,psv_array)
print(covariance_14[0][1])
print(corr14)
print(corrs14)

#%%
covariance_15 = np.cov(maxf3_array,diameter_array)
corr15, _ = scst.pearsonr(maxf3_array,diameter_array)
corrs15,v = scst.spearmanr(maxf3_array,diameter_array)
print(covariance_15[0][1])
print(corr15)
print(corrs15)

#%%
covariance_16 = np.cov(meanf3_array,diameter_array)
corr16, _ = scst.pearsonr(meanf3_array,diameter_array)
corrs16,v = scst.spearmanr(meanf3_array,diameter_array)
print(covariance_16[0][1])
print(corr16)
print(corrs16)

#%%
covariance_17 = np.cov(maxf3_array,depth_array)
corr17, _ = scst.pearsonr(maxf3_array,depth_array)
corrs17,v = scst.spearmanr(maxf3_array,depth_array)
print(covariance_17[0][1])
print(corr17)
print(corrs17)

#%%
covariance_18 = np.cov(meanf3_array,depth_array)
corr18, _ = scst.pearsonr(meanf3_array,depth_array)
corrs18,v = scst.spearmanr(meanf3_array,depth_array)
print(covariance_18[0][1])
print(corr18)
print(corrs18)

#%%
covariance_19 = np.cov(maxf4_array,psv_array)
corr19, _ = scst.pearsonr(maxf4_array,psv_array)
corrs19,v = scst.spearmanr(maxf4_array,psv_array)

print(covariance_19[0][1])
print(corr19)
print(corrs19)


#%%
covariance_20 = np.cov(meanf4_array,psv_array)
corr20, _ = scst.pearsonr(meanf4_array,psv_array)
corrs20,v = scst.spearmanr(meanf4_array,psv_array)
print(covariance_20[0][1])
print(corr20)
print(corrs20)

#%%
covariance_21 = np.cov(maxf4_array,diameter_array)
corr21, _ = scst.pearsonr(maxf4_array,diameter_array)
corrs21,v = scst.spearmanr(maxf4_array,diameter_array)
print(covariance_21[0][1])
print(corr21)
print(corrs21)

#%%
covariance_22 = np.cov(meanf4_array,diameter_array)
corr22, _ = scst.pearsonr(meanf4_array,diameter_array)
corrs22,v = scst.spearmanr(meanf4_array,diameter_array)
print(covariance_22[0][1])
print(corr22)
print(corrs22)

#%%
covariance_23 = np.cov(maxf4_array,depth_array)
corr23, _ = scst.pearsonr(maxf4_array,depth_array)
corrs23,v = scst.spearmanr(maxf4_array,depth_array)
print(covariance_23[0][1])
print(corr23)
print(corrs23)

#%%
covariance_24 = np.cov(meanf4_array,depth_array)
corr24, _ = scst.pearsonr(meanf4_array,depth_array)
corrs24,v = scst.spearmanr(meanf4_array,depth_array)
print(covariance_24[0][1])
print(corr24)
print(corrs24)'''