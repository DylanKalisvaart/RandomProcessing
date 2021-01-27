from numpy import genfromtxt

def csv_2_np(datafile):
    '''
    data = csv_2_np(datafile) converts a csv file to a numpy array
    
    Inputs:
        datafile: csv file
        
    Outputs:
        data: numpy array containing data
    '''
    return genfromtxt(datafile, delimiter=',')