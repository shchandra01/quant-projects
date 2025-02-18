
import numpy as np

N, d = 1000, 5  # 1000 time steps, 5 assets
rho = np.array([[1.0, 0.8, 0.5, 0.2, 0.1],  # Example correlation matrix
                [0.8, 1.0, 0.6, 0.3, 0.2],
                [0.5, 0.6, 1.0, 0.4, 0.3],
                [0.2, 0.3, 0.4, 1.0, 0.7],
                [0.1, 0.2, 0.3, 0.7, 1.0]])

# Cholesky decomposition (A is lower triangular)
A = np.linalg.cholesky(rho)

# Generate independent standard normal variables
Z = np.random.randn(N, d)

# Generate correlated Brownian motions
W = Z @ A  # Correct way to apply correlation

# Check empirical correlation (should be close to rho)
empirical_corr = np.corrcoef(W)
print(empirical_corr)
