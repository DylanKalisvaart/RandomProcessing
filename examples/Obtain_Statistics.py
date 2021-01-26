import numpy as np
import matplotlib.pyplot as plt

#load 1D random walk data from the data folder
random_walk_1D_data = np.load(r'raw_data/random_walk_1D_data.npy')


#calculate the mean (<x>) the mean squared (<x^2>)
mean = np.mean(random_walk_1D_data, axis = 0)
mean_sqrd = np.mean(random_walk_1D_data**2, axis = 0)
Nsteps = np.shape(mean)[0]
time = np.arange(Nsteps)

#Plot the mean squared and fit a linear trend
fig, ax = plt.subplots()
ax.plot(mean_sqrd)

[a, b] = np.polyfit(time, mean_sqrd, deg = 1)
ax.plot(time, b + a*time)

plt.savefig('processed_data/oneD_walk_mean_sqrd')

#calculate the diffusion coefficient
diff_coef = a*2

#Save extracted parameters
np.save('processed_data/random_walk_1D_mean', mean)
np.save('processed_data/random_walk_1D_meanSqrd', mean_sqrd)
np.save('processed_data/random_walk_1D_diffusioncoef', diff_coef)