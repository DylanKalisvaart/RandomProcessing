import numpy as np
import fit_functions
import matplotlib.pyplot as plt

a = 1
y0 = 0

xdata = np.linspace(0,1,101)
ydata = fit_functions.exp(xdata, a, y0) + 0.15*np.random.normal(0, .1, xdata.shape)

#find optimal parameters
popt = fit_functions.fit_exp(xdata, ydata)
print(popt)
#plot data
plt.plot(xdata, ydata, 'o', markersize = 2)
plt.plot(xdata, fit_functions.exp(xdata, *popt), linewidth = 2)

plt.savefig('Test exponential fit')