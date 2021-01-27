# Plot code, used to make plots in the bitcoin.py example
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def BTC_plot(data,mean,fit,figname):
    '''
    BTC_plot(data, mean, figname) plots the BTC data and mean in the BTC example
    
    Inputs:
        data: 1D numpy array containing BTC stock prices
        mean: float describing the mean of data
        figname: string, used as figname.png
    '''
    Nsteps = np.size(data)
    time = np.arange(Nsteps)

    #Make the final figure
    fig, axes = plt.subplots(1,1,figsize = (11,8))
    gridspec.GridSpec(1,1)
    ax1 = plt.subplot2grid((1,1), (0,0))

    #Set all figure settings
    tick_length = 5
    tick_width = 2
    pad_dist = 8
    label_pad_dist = 15
    scaling    = 'linear' 
    fonttype   = 'Arial' 
    main_title_fontsize = 30
    title_fontsize = 25
    label_fontsize = 17
    tick_label_fontsize   = 12
    legend_fontsize = 13
    mpfont = {'fontname': 'Arial'}

    #Plot the BTC price as a function of time
    ax1.plot(time, data)
    ax1.plot(time, np.ones(np.size(time))*mean, 'r--')
    ax1.plot(time, fit)
    ax1.legend(('BTC Price', 'Mean', 'Exponential fit'))

    #Customize all axes

    #the ticks
    ax1.tick_params(direction = 'in', labelsize = tick_label_fontsize, length = tick_length, width = tick_width, color = 'k', 
                  pad = pad_dist)

    #Set all x,y labels
    ax1.set_xlabel('steps', fontsize = label_fontsize )
    ax1.set_ylabel('position', fontsize = label_fontsize)

    #tight layout and save figure in the postprocess folder
    plt.tight_layout(pad = 2)
    plt.savefig('processed_data/' + figname + '.png')