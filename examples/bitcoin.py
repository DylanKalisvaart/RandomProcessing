import sys
sys.path.append('../..')

import numpy as np
import matplotlib.pyplot as plt

from RandomProcessing.data import data_importing as dimp
from RandomProcessing.preprocess import filtering as filt
from RandomProcessing.analyze import calc_statistics as stat
from RandomProcessing.analyze import regression as regr
from bitcoin_plots import BTC_plot

#Importing data
data = dimp.csv_2_np(r'raw_data/BTC_3months.csv')
ticks = np.arange(np.size(data))

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
popt = regr.fit_poly(ticks, data, degree = 3)
fit = regr.compute_poly(popt, ticks)

#Obtain sample mean of filtered data
mean_f = stat.mean(filtered_data)
popt_f = regr.fit_poly(ticks, data, degree=3)
fit_f = regr.compute_poly(popt_f, ticks)

#Analysis plots for raw and filtered data
BTC_plot(data, mean, fit, figname='analyze_raw_data')
BTC_plot(filtered_data, mean_f, fit_f, figname='analyze_filtered_data')