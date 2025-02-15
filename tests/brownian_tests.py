import numpy as np
import sys
sys.path.append(r'C:\Users\shiva\OneDrive\Documents\Quant Finance\quant-projects\src')
from brownian1d import geometric,arithmetic
import pricers
import matplotlib.pyplot as plt


initial = 100
paths = 10000
mu = 0.01
sigma = 0.1
timesteps = np.arange(0,1,0.01)
strike = 105

stn_ath = arithmetic(initial, timesteps, paths, mu, sigma)
stn_gm = geometric(initial, timesteps, paths, mu, sigma)

print(pricers.european_sim(initial, timesteps, paths, mu, sigma, strike))
print(pricers.asian_sim(initial, timesteps, paths, mu, sigma, strike))

plt.plot(stn_gm.T)
plt.show()