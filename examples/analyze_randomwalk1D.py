import sys
sys.path.append('../..')

#the custom function
from RandomProcessing.data import data_generation as dgen
from RandomProcessing.preprocess import filtering as filt
from RandomProcessing.analyze import calc_statistics

#The standard modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

#Parameters
Nwalks = 200
Nsteps = 10000
time = np.arange(Nsteps)

#generate random walk data
random_walk_1D_data = dgen.random_walk_1D(Nsteps, Nwalks)

#Filter one walk
filtered_data = filt.moving_average(random_walk_1D_data[0,:])

#Calculate statistics using the functions from the module
mean = calc_statistics.mean(random_walk_1D_data)
mean_sqrd = calc_statistics.mean_sqrd(random_walk_1D_data)
diff_coef = calc_statistics.diffusion_coefficient(random_walk_1D_data)


###########Make a summary Figure
##Fig 1 random walks, Fig 2 filtering data, Fig 3 diffusion, Fig 4 histogram
fig, axs = plt.subplots(2,2,figsize = (11,8))

#Set all figure settings
tick_length = 5
tick_width = 2
pad_dist = 8
label_pad_dist = 15
scaling    = 'linear' 
fonttype   = 'Arial' 
main_title_fontsize = 30
title_fontsize = 20
label_fontsize = 17
tick_label_fontsize   = 12
legend_fontsize = 13
mpfont = {'fontname': 'Arial'}


#Plot the random walks in the top left graph
for i in range(Nwalks): 
    axs[0,0].plot(time, random_walk_1D_data[i,:])

#plot filtered data in the bottom left graph
axs[1,0].plot(time, random_walk_1D_data[0,:], 'r--', linewidth = 0.5)
axs[1,0].plot(time, filtered_data, 'b', linewidth = 1)
axs[1,0].set_xlim([0,200])
axs[1,0].set_ylim([np.min(filtered_data[0:200]),np.max(filtered_data[0:200])])
axs[1,0].legend(['random walk', 'moving average'], fontsize = legend_fontsize)

#plot the mean squared value and the linear fit
axs[0,1].plot(time, mean_sqrd, linewidth = 1)
axs[0,1].plot(time, 0 + diff_coef/2*time, linewidth = 2)
axs[0,1].legend(['data', 'linear fit'], fontsize = legend_fontsize)

#Plot a histogram of the final positions
axs[1,1].hist(random_walk_1D_data[:,-1], bins = 20)


# Customize all axes

#the ticks
axs[0,0].tick_params(direction = 'in', labelsize = tick_label_fontsize, length = tick_length, width = tick_width, color = 'k', 
              pad = pad_dist)
axs[0,1].tick_params(direction = 'in', labelsize = tick_label_fontsize, length = tick_length, width = tick_width, color = 'k', 
              pad = pad_dist)
axs[1,0].tick_params(direction = 'in', labelsize = tick_label_fontsize, length = tick_length, width = tick_width, color = 'k', 
              pad = pad_dist)
axs[1,1].tick_params(direction = 'in', labelsize = tick_label_fontsize, length = tick_length, width = tick_width, color = 'k', 
              pad = pad_dist)

#Set all x,y labels
axs[0,0].set_xlabel('steps', fontsize = label_fontsize )
axs[0,0].set_ylabel('position', fontsize = label_fontsize)
axs[1,0].set_xlabel('steps', fontsize = label_fontsize )
axs[1,0].set_ylabel('position', fontsize = label_fontsize)
axs[0,1].set_xlabel('steps', fontsize = label_fontsize)
axs[0,1].set_ylabel(r'<$x^2$>', fontsize = label_fontsize)
axs[1,1].set_xlabel('position', fontsize = label_fontsize)
axs[1,1].set_ylabel('#instances', fontsize = label_fontsize)

#set all titles
axs[0,0].set_title('200 random walks', fontsize = title_fontsize)
axs[0,1].set_title('Moving average filter', fontsize = title_fontsize)
axs[1,0].set_title('Walker diffusion', fontsize = title_fontsize)
axs[1,1].set_title('Walker final positions', fontsize = title_fontsize)

#tight layout and save figure in the postprocess folder
plt.tight_layout(pad = 2)
plt.savefig('processed_data/1D_TotalFig')
