from scipy import optimize
import numpy as np

#The functions
def exp(x, k, a, y0):
    """
    Calculate the exponential y0 + k*exp(a*x) of all elements x in the input array
    
    Parameters
    ----------
    x: array_like
       Input values
    k: float
       multiplication factor before exponential
    a: float
       factor in exponential
    y0: float
        offset
        
    Returns
    -------
    out: ndarray or scalar
         Output array, element-wise y0 + k*exp(a*x). This is a scalar if x is a scalar
    """
    return y0 + k*np.exp(a*x)



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

def compute_poly(p,xdata):
    """
    Calculate polynomial series with coefficients p
    
    Parameters
    ----------
    xdata: array_like
       Input values
    p: polynomial coefficients
        
    Returns
    -------
    out: ndarray or scalar
         Output array, element-wise y0 + k*exp(a*x). This is a scalar if x is a scalar
    """
    return np.polyval(p,xdata)

def fit_poly(xdata,ydata,degree=3):    
    """
    Fit a polynomial series to the data
    
    Parameters
    ----------
    
    Returns
    -------
    popt: array
          Optimal values for the parameters so that the sum of the squared residuals of f(xdata, *popt) - ydata is minimized
    """
    p = np.polyfit(xdata,ydata,degree)
    return p