
import random
import matplotlib.pyplot as plt
import math

# Function to estimate π
def estimate_pi(N):
    inside = 0
    for _ in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside += 1
    return 4 * inside / N

# Sample sizes
N_values = [10, 100, 1000, 10000, 100000, 1000000 ]
pi_estimates = []

# Estimate π for each N
for N in N_values:
    pi = estimate_pi(N)
    pi_estimates.append(pi)
    print(f"N = {N}, π ≈ {pi:.6f}")

# Plot line chart
plt.figure(figsize=(10, 6))
plt.plot(N_values, pi_estimates, marker='o', linestyle='-', label='Estimated π')
plt.axhline(math.pi, color='red', linestyle='--', label='Actual π (3.14159)')
plt.xscale('log')
plt.xlabel('Number of Points (N)')
plt.ylabel('Estimated π')
plt.title('Monte Carlo Estimation of π vs Sample Size')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
