import sys
sys.path.append('../..')

import numpy as np
import matplotlib.pyplot as plt

from RandomProcessing.data import data_importing as dimp
from RandomProcessing.preprocess import filtering as filt
from RandomProcessing.analyze import calc_statistics as stat
from bitcoin_plots import BTC_plot

#Importing data
data = dimp.csv_2_np(r'raw_data/BTC_3months.csv')

#Filtering with moving average filter
filtered_data = filt.moving_average(data,size=5)

#Plot to compare data with filtered data
fig, (ax1, ax2) = plt.subplots(2,1)
ax1.plot(np.arange(np.size(data)), data)
ax2.plot(np.arange(np.size(data)), filtered_data)
ax2.set_xlabel('Ticks (price updates) since 27-10-2020')
ax1.set_ylabel('BTC Price ($)')
fig.savefig('processed_data/BTC_raw_and_filtered.png')

#Obtain sample mean of raw data
mean = stat.mean(data)

#Obtain sample mean of filtered data
mean_f = stat.mean(filtered_data)

#Analysis plots for raw and filtered data
BTC_plot(data, mean, figname='analyze_raw_data')
BTC_plot(filtered_data, mean_f, figname='analyze_filtered_data')