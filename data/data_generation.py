import numpy as np

def random_walk_1D(Nsteps = 10, Nwalks = 1):
    """Generate a Nwalks random walks of Nsteps time steps.
    
    Parameters:
        Nsteps (int): The number of time steps
        Nwalks (int): The number of random walks
    Returns:
        walk (ndarray): Nwalks random walk of Nsteps steps, 
        given by moving left (-1) or right (1)
    """
    
    return np.cumsum(2*np.round(np.random.rand(Nwalks, Nsteps))-1, axis = 1)