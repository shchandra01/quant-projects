import numpy as np

def geometric(initial, timesteps, paths, mu, sigma):
    random_paths = np.random.standard_normal((timesteps.shape[0], paths))
    return initial*np.exp((mu - sigma*sigma*0.5)*timesteps + sigma*np.sqrt(timesteps)*random_paths.T)

def arithmetic(initial, timesteps, paths, mu, sigma):
    random_paths = np.random.standard_normal((timesteps.shape[0], paths))
    return initial + mu*timesteps + sigma*np.sqrt(timesteps)*random_paths.T

def vasicek(initial, timesteps, paths, mu, sigma):
    random_paths = np.random.standard_normal((timesteps.shape[0], paths))
    return initial + mu*timesteps + sigma*np.sqrt(timesteps)*random_paths.T