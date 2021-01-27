import numpy as np
import matplotlib.pyplot as plt

def mean(random_walks):
    """
    Calculate the mean position of all walkers at every step
    
    Parameters
    ----------
    random_walks: array_like
                  Input array.
    
    Returns:
    --------
    mean: nd_array
          Mean at every step                
    
    """
    return np.mean(random_walks, axis = 0)
    
    
def mean_sqrd(random_walks):
    """
    Calculate the mean position of all walkers at every step
    
    Parameters
    ----------
    random_walks: array_like
                  Input array.
    
    Returns:
    --------
    mean_sqrd: nd_array
               mean squared position at every step                
    
    """
    return np.mean(random_walk_1D_data**2, axis = 0)
    
def diffusion_coefficient(random_walks):
    """
    Calculate the diffusion coefficient D of the random walkers
    D = <x^2>/(2*t) with <x^2> the mean position squared of the walkers at time t.
    Obtained by linear fit through the mean squared positions at different times t.
    
    Parameters
    ----------
    random_walks: array_like
                  Input array.
    
    Returns:
    --------
    D: float
       Diffusion coefficient                
    
    """

    Nsteps = np.shape(random_walks)[0]
    time = np.arange(Nsteps)
    [a, b] = np.polyfit(time, mean_sqrd(random_walks), deg = 1)
    
    #calculate the diffusion coefficient
    D = a*2
    
    return D
