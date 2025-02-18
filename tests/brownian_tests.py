import numpy as np
import sys
sys.path.append(r'C:\Users\shiva\OneDrive\Documents\Quant Finance\quant-projects\src')
from brownian_1d import geometric,arithmetic
import pricers
import matplotlib.pyplot as plt


initial = 100
paths = 10000
mu = 0.01
sigma = 0.1
timesteps = np.arange(0,1,0.01)
strike = 100

stn_ath = arithmetic(initial, timesteps, paths, mu, sigma)
stn_gm = geometric(initial, timesteps, paths, mu, sigma)

print("European call price: ",pricers.european(initial, timesteps, paths, mu, sigma, strike))
print("Asian call price: ",pricers.asian(initial, timesteps, paths, mu, sigma, strike))
print("Geometric Asian call price: ",pricers.geometric_asian(initial, timesteps, paths, mu, sigma, strike))
print("Lookback call price: ",pricers.lookback(initial, timesteps, paths, mu, sigma))