# GPGN268 - Numpy and basics plotting
#**Author:** Gigi Albers
#This notebook uses meteorological data from the Denver water department to introduce basic Python concepts.

import numpy as np
import matplotlib.pyplot as plt

# Load max temperature data into a numpy array.
# According to the README this corresponds to monthly maximum temperatures
# from 2000 to 2022 at the Dever Water Department meteorological station.
tmax = np.loadtxt(fname='../data/meteo_denver_tmax_2000_2022.txt', delimiter='\t')

type(tmax)
tmax.dtype
print(tmax.shape)

print('first value in tmax:', tmax[0, 0])
print('first value in tmax:', tmax[9, 16])