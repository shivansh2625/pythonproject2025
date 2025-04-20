

import numpy as np
import matplotlib.pyplot as plt


def f(x): #Define the function to integrate
    return x**2  #Changeable function

#Input integration limits and number of subintervals
a = 0      # start of interval
b = 5      # end of interval
n = 10     # number of subintervals

#Implement the Trapezoidal Rule function
def trapezoidal_rule(f,a,b,n):
    h = (b - a)/n
    x = np.linspace(a,b,n+1)
    y = f(x)
    area = h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])
    return area, x, y

#Compute approximation
area, x_vals, y_vals = trapezoidal_rule(f, a, b, n)
print(f"Approximate integral using Trapezoidal Rule: {area}")

#Plot the function and trapezoids
plt.figure(figsize=(8, 5))
x_fine = np.linspace(a, b, 1000)
plt.plot(x_fine, f(x_fine), 'r', label='f(x)')
plt.fill_between(x_vals, y_vals, color='yellow', alpha=0.5, step='mid', label='Trapezoids')
plt.plot(x_vals, y_vals, 'ko-')
plt.title('Trapezoidal Rule Approximation')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

