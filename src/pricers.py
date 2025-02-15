import numpy as np
from brownian1d import geometric

def european_sim(initial, timesteps, sim, mu, sigma, strike, flavor='call'):
    s_t = geometric(initial, timesteps, sim, mu, sigma)
    if flavor == 'call':
        return np.mean(np.maximum(s_t[:,-1] - strike,0))
    else:
        return np.mean(np.maximum(strike - s_t[:,-1],0))


def asian_sim(initial, timesteps, sim, mu, sigma, strike, flavor='call'):
    s_t = geometric(initial, timesteps, sim, mu, sigma)
    if flavor == 'call':
        return np.mean(np.maximum(np.mean(s_t,axis=1) - strike,0))
    else:
        return np.mean(np.maximum(strike - np.mean(s_t,axis=1),0))

def geometric_asian(initial, timesteps, sim, mu, sigma, strike, flavor='call'):
    s_t = geometric(initial, timesteps, sim, mu, sigma)
    if flavor == 'call':
        return np.mean(np.maximum(np.mean(s_t,axis=1) - strike,0))
    else:
        return np.mean(np.maximum(strike - np.mean(s_t,axis=1),0))

def lookback(initial, timesteps, sim, mu, sigma, strike, flavor='call'):
    s_t = geometric(initial, timesteps, sim, mu, sigma)
    if flavor == 'call':
        return np.mean(np.maximum(np.mean(s_t,axis=1) - strike,0))
    else:
        return np.mean(np.maximum(strike - np.mean(s_t,axis=1),0))
    
def european_analytic():
    pass
