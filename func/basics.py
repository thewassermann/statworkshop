from numpy import sum as sum_

def var(s_1, unbiased=True):
    """
    Returns the variance of a series.
    
    Parameters
    ----------
    
        s_1 : np.array
            A series

        biased : boolean

    Returns
    -------
    
        variance : float
    """
    # calculation
    try:
        n = len(s_1)
    except TypeError:
        raise TypeError('Not a valid array passed to `var`')

    # change for biased/unbiased
    # will use sample variance (unbiased) as default
    e_x = sum_(s_1) / n

    # if s_1 has one element
    if n <= 1:
        return 0.
    
    if unbiased:
        n -= 1

    return sum_((s_1 - e_x)**2) / n

def cov(s_1, s_2):
    """
    Returns the covariance of two series. Degrees of Freedom set to 0.
    
    Parameters
    ----------
    
        s_1 : np.array
            First series
            
        s_2 : np.array
            Second series
            
    Returns
    -------
    
        covariance : float
    """
    # set the length of the series
    n = len(s_1)
    
    # check that both series are the same length
    # else raise an error
    if len(s_2) != n:
        raise ValueError('Unmatched number of elements in series')

    # calculation (E[XY] - E[X]E[Y])
    # expectations empirically estimated
    sigma_xy = sum_(s_1 * s_2) / n 
    sigma_x = sum_(s_1) / n
    sigma_y = sum_(s_2) / n
    return sigma_xy - (sigma_x * sigma_y)