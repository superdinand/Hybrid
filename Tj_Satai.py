import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot as plt

data = pd.read_excel('Daily_Data_Satai.xlsx')

Hours = data.iloc[:,0].values
Demand = data.iloc[:,1].values
Irradiance = data.iloc[:, 2].values


PV_Cap = 1500 #kW
PV_Eff = 0.9 #90% efficiency

E_PV = (PV_Cap * Irradiance)/1000
E_Surplus = E_PV - Demand

plt.plot(Hours, E_PV)
plt.plot(Hours, Demand)
plt.legend(['E_PV', 'E_Demand'])
plt.xlabel("Hours")
plt.ylabel("Energy in kWH")




Q1=[]
Q2=[]
for i in E_Surplus:
    if i < 0:
        Q1 = 0
        Q2 = 100
    
    else:
        Q1 = 1000/3600
        Q2 = 0
        

print (Q1)