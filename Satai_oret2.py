#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 11:16:01 2020

@author: superdinand
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('Daily_Data_Satai.xlsx')

Hours = data.iloc[0:100:,0].values
Demand = data.iloc[0:100:,1].values
Irradiance = data.iloc[0:100:, 2].values


PV_Cap = 1500 #kW
PV_Eff = 0.9 #90% efficiency

E_PV = (PV_Cap * Irradiance)/1000
E_Surplus = E_PV - Demand

#plt.plot(Hours, E_PV)
#plt.plot(Hours, Demand)
#plt.legend(['E_PV', 'E_Demand'])
#plt.xlabel("Hours")
#plt.ylabel("Energy in kWH")

a = 1;  b = 100                       
N = b-1                               
#dt = (b - a)/N                       
R1 = np.zeros(N+1)
R2 = np.zeros(N+1)                     
Q1 = []
Q2 = []
R1[0] = 1000
R2[0] = 5000



for i in range(0, N, 1):
    for x in E_Surplus:
        if x < 0 and R1[i] > 0 and R1[i] < ((-E_Surplus*1000 / 1000*9.8*8*0.9)*3600):
            Q1.append(R1/3600)
            Q2.append(0)
        else:
            Q1.append(1000/3600)
            Q2.append(0)
        
for i in range(0, N, 1):
    R1[i+1] = R1[i] + Q2[i] - Q1[i]
    
for i in range(0, N, 1):           
    R2[i+1] = R2[i] - Q2[i]+ Q1[i]


    
E_hydro = []
for j in Q1:
    E_hydro.append((1000*j*9.8*8*0.9*1)/1000) #in kWH
    

        




    


time = np.linspace(1, 100, N+1)
plt.plot(time, R1, 'bo-', R2, 'r', E_hydro, 'g')
plt.title('Tj_Satai')
plt.legend(['Upper Reservoir', 'Lower Reservoir', 'Energy from hydro'], loc='upper left')
plt.xlabel('t (hour)')
plt.ylabel('V (L)')
plt.show()