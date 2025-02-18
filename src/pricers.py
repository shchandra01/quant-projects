import numpy as np
from brownian_1d import geometric
from brownian_nd import arithmetic

def european(initial, timesteps, sim, mu, sigma, strike, flavor='call'):
    s_t = geometric(initial, timesteps, sim, mu, sigma)
    if flavor == 'call':
        return np.mean(np.maximum(s_t[:,-1] - strike,0))
    else:
        return np.mean(np.maximum(strike - s_t[:,-1],0))


def asian(initial, timesteps, sim, mu, sigma, strike, flavor='call'):
    s_t = geometric(initial, timesteps, sim, mu, sigma)
    if flavor == 'call':
        return np.mean(np.maximum(np.mean(s_t,axis=1) - strike,0))
    else:
        return np.mean(np.maximum(strike - np.mean(s_t,axis=1),0))

def geometric_asian(initial, timesteps, sim, mu, sigma, strike, flavor='call'):
    s_t = geometric(initial, timesteps, sim, mu, sigma)
    if flavor == 'call':
        return np.mean(np.maximum(np.exp(np.mean(np.log(s_t),axis=1)) - strike,0))
    else:
        return np.mean(np.maximum(strike - np.exp(np.mean(np.log(s_t),axis=1)),0))

def lookback(initial, timesteps, sim, mu, sigma, flavor='call'):
    s_t = geometric(initial, timesteps, sim, mu, sigma)
    if flavor == 'call':
        return np.mean(np.maximum(np.max(s_t,axis=1) - s_t[:,-1],0))
    else:
        return np.mean(np.maximum(s_t[:,-1] - np.max(s_t,axis=1),0))
    
def european_analytic():
    pass


def basket(initial, timesteps, paths, mu, corr_mat, vols, weights, strike):
    all_paths = arithmetic(initial, timesteps, paths, mu, corr_mat, vols)
    ST = all_paths[:,:,-1] # mu.shape[0], paths, timesteps.shape[0]
    intrinsic = np.maximum(np.dot(ST.T,weights) - strike, 0)
    return np.mean(intrinsic)
