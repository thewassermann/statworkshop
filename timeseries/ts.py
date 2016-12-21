from statworkshop.func.basics import cov, var
from statworkshop.plotting.plotting import single_ts_plot
import matrplotlib.pyplot as plt

def acvf(ts, max_lag, plot=True):
    """
    Function to return the value of the autocovariance
    function of the time-series `ts` up to max_lags.
    
    Parameters
    ----------
    
        ts : np.array
            np.array of a timeseries
            
        max_lag : int
            the largest lag given for the acvf. If the
            `max_lag` exceeds the largest lag possible for
            the data, the maximum lag possible will be returned.
            
    Returns
    -------
    
        acvf_array : np.array
            array containing `max_lag` calculations of the acvf
            for time series `ts`
    """
    # check if max_lag less than ts
    if len(ts) < max_lag:
        max_lag = len(ts)
        
    # create np array to store values
    acvf_array = np.empty((max_lag))

    # get autocovariances
    for i in xrange(max_lag):
        acvf_array[i] = cov(ts[i:], ts[:(len(ts)-i)])
        
    # for graphical output
    if plot:
        fig, ax = plt.subplots(1,1)
        ax  = single_ts_plot(
            acvf_array,
            ax,
            'Autocovariance Function',
            'ACVF',
        )
        plt.show()
    else:
        return acvf_array


def acf(ts, max_lag, plot=True):
    """
    Function to return the value of the autocorrelation
    function of the time-series `ts` up to max_lags.
    
    Parameters
    ----------
    
        ts : np.array
            np.array of a timeseries
            
        max_lag : int
            the largest lag given for the acf. If the
            `max_lag` exceeds the largest lag possible for
            the data, the maximum lag possible will be returned.
            
    Returns
    -------
    
        acf_array : np.array
            array containing `max_lag` calculations of the acf
            for time series `ts`
    """
    # use the autocovariance function of lag 0 to calculate the acf
    acvf_ = acvf(ts, max_lag)
    acf_ = acvf_ / acvf_[0]

    # for graphical output
    if plot:
        fig, ax = plt.subplots(1,1)
        ax  = single_ts_plot(
            acf_,
            ax,
            'Autocorrelation Function',
            'ACF',
        )
        plt.show()
    else:
        return acvf_array