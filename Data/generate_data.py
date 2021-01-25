import functions.generating_functions as gfuncs
import numpy as np
import matplotlib.pyplot as plt

#Input parameters
Nsteps = 10000
Nwalks = 200

#Generate the 1D random walks
times = np.arange(Nsteps)
oneD_walk = gfuncs.random_walk_1D(Nsteps, Nwalks)
oneD_walk_position = np.cumsum(oneD_walk, axis = 1)


#Plot the Random walks
fig, ax = plt.subplots()
for i in range(Nwalks):
    ax.plot(times, oneD_walk_position[i,:])

#Save the figure and data
np.save('data/random_walk_1D_data', oneD_walk_position)
plt.savefig('data/OneD_walk')