import sys
sys.path.append('../..')

import numpy as np
import matplotlib.pyplot as plt

from RandomProcessing.data import data_importing as dimp
from RandomProcessing.preprocess import filtering as filt
from RandomProcessing.analyze import calc_statistics as stat

data = dimp.csv_2_np(r'raw_data/BTC_3months.csv')
filtered_data = filt.moving_average(data,size=5)

fig, (ax1, ax2) = plt.subplots(2,1)
ax1.plot(np.arange(np.size(data)), data)
ax2.plot(np.arange(np.size(data)), filtered_data)
ax2.set_xlabel('Ticks (price updates) since 27-10-2020')
ax1.set_ylabel('BTC Price ($)')
fig.savefig('BTC_3m.png')