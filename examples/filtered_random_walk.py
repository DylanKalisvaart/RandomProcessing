import sys
sys.path.append('../..')

from RandomProcessing.data import data_generation as dgen
from RandomProcessing.preprocess import filtering as filt
import numpy as np
import matplotlib.pyplot as plt

Nwalks = 1
Nsteps = 100

#Generate, then filter data
data = dgen.random_walk_1D(Nsteps, Nwalks)
filtered_data = filt.moving_average(data)

#Plotting
fig, ax = plt.subplots()
ax.plot(np.arange(Nsteps), data.T, 'r-')
ax.plot(np.arange(Nsteps), filtered_data.T, 'b--')
ax.set_xlabel('Time step')
ax.set_ylabel('Magnitude')
fig.savefig('filtered_random_walk.png')