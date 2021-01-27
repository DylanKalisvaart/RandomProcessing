from numpy import genfromtxt

def csv_2_np(datafile,stripleft=2, stripup = 1):
    '''
    data = csv_2_np(datafile) converts a csv file to a numpy array
    
    Inputs:
        datafile: csv file
        stripleft: amount of columns on the left to be removed (usually reserved for text). Default = 2
        stripup: amount of rows on the top to be removed (usually reserved for text). Default = 1
        
    Outputs:
        data: numpy array containing data
    '''
    npdata = genfromtxt(datafile, delimiter=',')
    data = npdata[stripup::, stripleft::]
    return data.flatten()