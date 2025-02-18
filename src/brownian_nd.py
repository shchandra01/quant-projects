import numpy as np
from scipy.stats import multivariate_normal

def cholesky():
    pass

def geometric(initial, timesteps, paths, mu, sigma):
    random_paths = multivariate_normal(mu, sigma)
    Z = random_paths.rvs(10)
    return initial*np.exp((mu - sigma*sigma*0.5)*timesteps + sigma*np.sqrt(timesteps)*random_paths.T)

def arithmetic(initial, timesteps, paths, mu, corr_mat, vols):
    #alt 1
    cov = np.diag(vols)*corr_mat*np.diag(vols)
    # print(corr_mat)
    #alt 2
    A = np.linalg.cholesky(cov)
    X = np.zeros((mu.shape[0], paths, timesteps.shape[0]))
    for time_idx, time in enumerate(timesteps):
        random_paths = np.random.standard_normal((paths, mu.shape[0]))
        corr_paths = A @ random_paths.T
        X[:,:,time_idx] = initial.reshape(5,1) + (mu*time).reshape(5,1) + corr_paths*(np.sqrt(time))

    return X