from scipy import optimize
import numpy as np

#The functions
def exp(x, a, y0):
    """
    Calculate the exponential y0 + exp(a*x) of all elements x in the input array
    
    Parameters
    ----------
    x: array_like
       Input values
    a: float
       factor in exponential
    y0: float
        offset
        
    Returns
    -------
    out: ndarray or scalar
         Output array, element-wise y0 + exp(a*x). This is a scalar if x is a scalar
    """
    return y0 + np.exp(a*x)



def fit_exp(xdata, ydata):
    """
    Fit the function exp to the data
    
    Parameters
    ----------
    
    Returns
    -------
    popt: array
          Optimal values for the parameters so that the sum of the squared residuals of f(xdata, *popt) - ydata is minimized
    """
    popt,pcov = optimize.curve_fit(exp, xdata, ydata)
    
    return popt
