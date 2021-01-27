import sys
sys.path.append('../..')

import numpy as np
import matplotlib.pyplot as plt

from RandomProcessing.data import data_importing as dimp
from RandomProcessing.preprocess import filtering as filt
from RandomProcessing.analyze import calc_statistics as stat

data = dimp.csv_2_np(r'raw_data/BTC_3months.csv')


fig, ax = plt.subplots()
ax.plot(np.arange(np.size(data)), data)
fig.savefig('BTC_3m.png')