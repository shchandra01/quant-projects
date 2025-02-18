import numpy as np
import sys
sys.path.append(r'C:\Users\shiva\OneDrive\Documents\Quant Finance\quant-projects\src')
from brownian_nd import geometric,arithmetic
import pricers
import matplotlib.pyplot as plt


initial = np.array([100, 200, 300, 400, 500])
corr_mat = np.matrix([[1, 0.1, -0.1, 0, 0], [0.1, 1, 0, 0, 0.2], [-0.1, 0, 1, 0, 0], [0, 0, 0, 1, 0.15], [0, 0.2, 0, 0.15, 1]])
vols = np.array([0.1, 0.12, 0.13, 0.09, 0.11])
paths = 10000
mu = np.array([0.01]*5)
timesteps = np.arange(0,1,0.01)
strikes = [100, 200, 300, 400, 500]
cov = np.diag(vols)*corr_mat*np.diag(vols)
strike = 300
stn_ath = arithmetic(initial, timesteps, paths, mu, corr_mat, vols)
weights = np.array([0.2]*5)

# stn_gm = geometric(initial, timesteps, paths, mu, sigma)

# print("European call price: ",pricers.european(initial, timesteps, paths, mu, sigma, strike))
# print("Asian call price: ",pricers.asian(initial, timesteps, paths, mu, sigma, strike))
# print("Geometric Asian call price: ",pricers.geometric_asian(initial, timesteps, paths, mu, sigma, strike))
# print("Lookback call price: ",pricers.lookback(initial, timesteps, paths, mu, sigma))
print("Basket call price: ", pricers.basket(initial, timesteps, paths, mu, corr_mat, vols, weights, strike))

