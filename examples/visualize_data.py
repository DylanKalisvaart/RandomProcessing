import sys
sys.path.append('../..')

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

#load 1D random walk data + statistics
random_walk_1D_data = np.load(r'../data/data/random_walk_1D_data.npy')
mean = np.load(r'../analyze/random_walk_1D_mean.npy')
mean_sqrd = np.load(r'../RandomProcessing/analyze/random_walk_1D_meanSqrd.npy')
diff_coef = np.load(r'../RandomProcessing/analyze/random_walk_1D_diffusioncoef.npy')

Nsteps = np.shape(random_walk_1D_data)[1]
Nwalks = np.shape(random_walk_1D_data)[0]
time = np.arange(Nsteps)


#Make the final figure
fig, axes = plt.subplots(2,2,figsize = (11,8))
gridspec.GridSpec(2,2)
ax1 = plt.subplot2grid((2,2), (0,0), colspan=1, rowspan=2)
ax2 = plt.subplot2grid((2,2), (0,1))
ax3 = plt.subplot2grid((2,2), (1,1))

#Set all figure settings
tick_length = 5
tick_width = 2
pad_dist = 8
label_pad_dist = 15
scaling    = 'linear' 
fonttype   = 'Arial' 
main_title_fontsize = 30
title_fontsize = 25
label_fontsize = 17
tick_label_fontsize   = 12
legend_fontsize = 13
mpfont = {'fontname': 'Arial'}


#Plot the random walks
for i in range(Nwalks): 
    ax1.plot(time, random_walk_1D_data[i,:])

#plot the mean squared value and the linear fit
ax2.plot(time, mean_sqrd, linewidth = 1)
ax2.plot(time, 0 + diff_coef/2*time, linewidth = 2)
ax2.legend(['data', 'linear fit'], fontsize = legend_fontsize)

#Plot a histogram of the final positions
ax3.hist(random_walk_1D_data[:,-1], bins = 20)


#Customize all axes

#the ticks
ax1.tick_params(direction = 'in', labelsize = tick_label_fontsize, length = tick_length, width = tick_width, color = 'k', 
              pad = pad_dist)
ax2.tick_params(direction = 'in', labelsize = tick_label_fontsize, length = tick_length, width = tick_width, color = 'k', 
              pad = pad_dist)
ax3.tick_params(direction = 'in', labelsize = tick_label_fontsize, length = tick_length, width = tick_width, color = 'k', 
              pad = pad_dist)

#Set all x,y labels
ax1.set_xlabel('steps', fontsize = label_fontsize )
ax1.set_ylabel('position', fontsize = label_fontsize)
ax2.set_xlabel('steps', fontsize = label_fontsize)
ax2.set_ylabel(r'<$x^2$>', fontsize = label_fontsize)
ax3.set_xlabel('position', fontsize = label_fontsize)
ax3.set_ylabel('#instances', fontsize = label_fontsize)

#tight layout and save figure in the postprocess folder
plt.tight_layout(pad = 2)
plt.savefig('postprocess/1D_summaryFig')