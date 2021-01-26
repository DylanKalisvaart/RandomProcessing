from scipy.ndimage.filters import uniform_filter1d

def moving_average(data,size=3):
    '''
    filtered_data = moving_average(data) uses a moving average filter to reduce variance in the data. Boundaries are 
    included, as to not reduce the size of the data.
    
    Inputs:
        data: numpy 2D-array (size: amount of realizations, amount of time steps) containing random process data
        size: amount of data points included in moving average filter (standard size = 3)
    
    Outputs:
        filtered_data: moving average filtered data
    '''
    return uniform_filter1d(data, size)