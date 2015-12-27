# Linear regression x => using gradient descent
#
# Example: gradient_descent(0, 0, 0.01, 1000)
#

import numpy as np

x_1 = [600, 200, 300, 523, 234, 123] # feature 1 samples
x_2 = [3, 2.5, 4, 5, 5, 3] # feature 2 samples
x = x_1 # for single-feature regression
m = len(x_1)
xs = np.vstack(([1] * m, x_1, x_2)) # for multi-feature regression

y = [20000, 12000, 14020, 21000, 13210, 11500] # values to predict

assert len(x) == len(y)

def h(theta_0, theta_1):
    return theta_0 + np.multiply(theta_1, x)

def J(theta_0, theta_1):
    return 0.5/m * np.sum((h(theta_0, theta_1) - y) ** 2)

def dJ_0(theta_0, theta_1): # dJ / dtheta_0
    return 1.0/m * np.sum(h(theta_0, theta_1) - y)

def dJ_1(theta_0, theta_1): # dJ / dtheta_0
    return 1.0/m * np.sum(np.multiply(h(theta_0, theta_1) - y, x))

def normalize(x):
    return (x - np.mean(x)) / (np.max(x) - np.min(x) + 1)

def denormalize(x, theta_0, theta_1):
    range = np.max(x) - np.min(x) + 1
    return theta_0 - np.mean(x) * theta_1 / range, theta_1 / range

def gradient_descent(theta_0, theta_1, alpha, steps):
    global x
    x_restore = x
    x = normalize(x)
    print x
    for i in range(steps):
        d_0 = dJ_0(theta_0, theta_1)
        d_1 = dJ_1(theta_0, theta_1)
        theta_0 -= alpha * d_0
        theta_1 -= alpha * d_1
        j = J(theta_0, theta_1)
        print 'Step #{0}: {1}, {2} => {3} ({4}, {5})'.format(i, theta_0, theta_1, j, d_0, d_1)
    x = x_restore
    theta_0, theta_1 = denormalize(x, theta_0, theta_1)
    print theta_0, theta_1

"""
def h_(theta): # [theta_0, theta_1, ...]
    return np.dot(theta, xs)

def J_(theta):
    m = len(xs[0])
    return 0.5/m * np.sum((h(theta) - y) ** 2)
    """
