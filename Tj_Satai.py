import numpy as np


Hours, Demand, Irradiance, EPV, Ehydro, Natural_Flow, BP_Flow = np.loadtxt("mydata_Teshima.csv", skiprows = 1, unpack=True, delimiter=',')