import sys
sys.path.append('../..')

import numpy as np
import matplotlib.pyplot as plt
from RandomProcessing.data import data_generation as dgen
from RandomProcessing.analyze import calc_statistics

#Parameters
Nwalks = 200
Nsteps = 10000
time = np.arange(Nsteps)

#generate random walk data
random_walk_1D_data = dgen.random_walk_1D(Nsteps, Nwalks)

#Calculate statistics using the functions from the module
mean = calc_statistics.mean(random_walk_1D_data)
mean_sqrd = calc_statistics.mean_sqrd(random_walk_1D_data)
diff_coef = calc_statistics.diffusion_coefficient(random_walk_1D_data)


#Plot the mean squared position <x^2>, with the best linear fit
plt.plot(time, mean_sqrd)
plt.plot(time, 0 + time*diff_coef/2)
