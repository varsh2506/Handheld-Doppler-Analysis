#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 16:54:13 2019

@author: kshama
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as scst


with open("DataX.csv",mode="r") as f:
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

plt.scatter(psv_array,maxf1_array)
plt.show()  

#%%
covariance_1 = np.cov(maxf1_array,psv_array)
corr1, _ = scst.pearsonr(maxf1_array,psv_array)
corrs1,v = scst.spearmanr(maxf1_array,psv_array)
print(covariance_1[0][1])
print('corr1 ',corr1)
print('corrs1 ',corrs1)

#%%
covariance_2 = np.cov(meanf1_array,psv_array)
corr2, _ = scst.pearsonr(meanf1_array,psv_array)
corrs2,v = scst.spearmanr(meanf1_array,psv_array)
print(covariance_2[0][1])
print('corr2 ',corr2)
print('corrs2 ',corrs2)

#%%
covariance_3 = np.cov(maxf1_array,diameter_array)
corr3, _ = scst.pearsonr(maxf1_array,diameter_array)
corrs3,v = scst.spearmanr(maxf1_array,diameter_array)
print(covariance_3[0][1])
print('corr3 ',corr3)
print('corrs3 ',corrs3)

#%%
covariance_4 = np.cov(meanf1_array,diameter_array)
corr4, _ = scst.pearsonr(meanf1_array,diameter_array)
corrs4,v = scst.spearmanr(meanf1_array,diameter_array)
print(covariance_4[0][1])
print('corr4 ',corr4)
print('corrs4 ',corrs4)

#%%
covariance_5 = np.cov(maxf1_array,depth_array)
corr5, _ = scst.pearsonr(maxf1_array,depth_array)
corrs5,v = scst.spearmanr(maxf1_array,depth_array)
print(covariance_5[0][1])
print('corr5 ',corr5)
print('corrs5 ',corrs5)

#%%
covariance_6 = np.cov(meanf1_array,depth_array)
corr6, _ = scst.pearsonr(meanf1_array,depth_array)
corrs6,v = scst.spearmanr(meanf1_array,depth_array)
print(covariance_6[0][1])
print('corr6 ',corr6)
print('corrs6 ',corrs6)

#%%
covariance_7 = np.cov(maxf2_array,psv_array)
corr7, _ = scst.pearsonr(maxf2_array,psv_array)
corrs7,v = scst.spearmanr(maxf2_array,psv_array)
print(covariance_7[0][1])
print('corr7 ',corr7)
print('corrs7 ',corrs7)

#%%
covariance_8 = np.cov(meanf2_array,psv_array)
corr8, _ = scst.pearsonr(meanf2_array,psv_array)
corrs8,v = scst.spearmanr(meanf2_array,psv_array)
print(covariance_8[0][1])
print('corr8 ',corr8)
print('corrs8 ',corrs8)
#%%
covariance_9 = np.cov(maxf2_array,diameter_array)
corr9, _ = scst.pearsonr(maxf2_array,diameter_array)
corrs9,v = scst.spearmanr(maxf2_array,diameter_array)
print(covariance_9[0][1])
print('corr9 ',corr9)
print('corrs9 ',corrs9)

#%%
covariance_10 = np.cov(meanf2_array,diameter_array)
corr10, _ = scst.pearsonr(meanf2_array,diameter_array)
corrs10,v = scst.spearmanr(meanf2_array,diameter_array)
print(covariance_10[0][1])
print('corr10 ',corr10)
print('corrs10 ',corrs10)

#%%
covariance_11 = np.cov(maxf2_array,depth_array)
corr11, _ = scst.pearsonr(maxf2_array,depth_array)
corrs11,v = scst.spearmanr(maxf2_array,depth_array)
print(covariance_11[0][1])
print('corr11 ',corr11)
print('corrs11 ',corrs11)

#%%
covariance_12 = np.cov(meanf2_array,depth_array)
corr12, _ = scst.pearsonr(meanf2_array,depth_array)
corrs12,v = scst.spearmanr(meanf2_array,depth_array)
print(covariance_12[0][1])
print('corr12 ',corr12)
print('corrs12 ',corrs12)
#%%
#%%
covariance_13 = np.cov(maxf3_array,psv_array)
corr13, _ = scst.pearsonr(maxf3_array,psv_array)
corrs13,v = scst.spearmanr(maxf3_array,psv_array)
print(covariance_13[0][1])
print('corr13 ',corr13)
print('corrs13 ',corrs13)
#%%
covariance_14 = np.cov(meanf3_array,psv_array)
corr14, _ = scst.pearsonr(meanf3_array,psv_array)
corrs14,v = scst.spearmanr(meanf3_array,psv_array)
print(covariance_14[0][1])
print('corr14 ',corr14)
print('corrs14 ',corrs14)

#%%
covariance_15 = np.cov(maxf3_array,diameter_array)
corr15, _ = scst.pearsonr(maxf3_array,diameter_array)
corrs15,v = scst.spearmanr(maxf3_array,diameter_array)
print(covariance_15[0][1])
print('corr15 ',corr15)
print('corrs15 ',corrs15)

#%%
covariance_16 = np.cov(meanf3_array,diameter_array)
corr16, _ = scst.pearsonr(meanf3_array,diameter_array)
corrs16,v = scst.spearmanr(meanf3_array,diameter_array)
print(covariance_16[0][1])
print('corr16 ',corr16)
print('corrs16 ',corrs16)

#%%
covariance_17 = np.cov(maxf3_array,depth_array)
corr17, _ = scst.pearsonr(maxf3_array,depth_array)
corrs17,v = scst.spearmanr(maxf3_array,depth_array)
print(covariance_17[0][1])
print('corr17 ',corr17)
print('corrs17 ',corrs17)

#%%
covariance_18 = np.cov(meanf3_array,depth_array)
corr18, _ = scst.pearsonr(meanf3_array,depth_array)
corrs18,v = scst.spearmanr(meanf3_array,depth_array)
print(covariance_18[0][1])
print('corr18 ',corr18)
print('corrs18 ',corrs18)

#%%
covariance_19 = np.cov(maxf4_array,psv_array)
corr19, _ = scst.pearsonr(maxf4_array,psv_array)
corrs19,v = scst.spearmanr(maxf4_array,psv_array)

print(covariance_19[0][1])
print('corr19 ',corr19)
print('corrs19 ',corrs19)


#%%
covariance_20 = np.cov(meanf4_array,psv_array)
corr20, _ = scst.pearsonr(meanf4_array,psv_array)
corrs20,v = scst.spearmanr(meanf4_array,psv_array)
print(covariance_20[0][1])
print('corr20 ',corr20)
print('corrs20 ',corrs20)

#%%
covariance_21 = np.cov(maxf4_array,diameter_array)
corr21, _ = scst.pearsonr(maxf4_array,diameter_array)
corrs21,v = scst.spearmanr(maxf4_array,diameter_array)
print(covariance_21[0][1])
print('corr21 ',corr21)
print('corrs21 ',corrs21)

#%%
covariance_22 = np.cov(meanf4_array,diameter_array)
corr22, _ = scst.pearsonr(meanf4_array,diameter_array)
corrs22,v = scst.spearmanr(meanf4_array,diameter_array)
print(covariance_22[0][1])
print('corr22 ',corr22)
print('corrs22 ',corrs22)

#%%
covariance_23 = np.cov(maxf4_array,depth_array)
corr23, _ = scst.pearsonr(maxf4_array,depth_array)
corrs23,v = scst.spearmanr(maxf4_array,depth_array)
print(covariance_23[0][1])
print('corr23 ',corr23)
print('corrs23 ',corrs23)

#%%
covariance_24 = np.cov(meanf4_array,depth_array)
corr24, _ = scst.pearsonr(meanf4_array,depth_array)
corrs24,v = scst.spearmanr(meanf4_array,depth_array)
print(covariance_24[0][1])
print('corr24 ',corr24)
print('corrs24 ',corrs24)