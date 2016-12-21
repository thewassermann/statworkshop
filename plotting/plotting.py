"""
A collection of plotting functions for the statworkshop 
library
"""

def single_ts_plot(arr, ax, title, type_, ci_flag=True):
    """
    Function to take in an array and produce a 
    matplotlib bar chart on an axis
    """
    
    # formatting
    ax.set_title(title)
    ax.set_xlabel('Lags')
    ax.set_ylabel(type_)
    
    # plot points
    ax.bar(xrange(len(arr)), arr, alpha=0.4, color='blue')
    
    # confidence intervals for white noise process
    if ci_flag:
        ax.axhline(1 / (len(arr)**.5), color='red', ls='--')
        ax.axhline(-1 / (len(arr)**.5), color='red', ls='--')