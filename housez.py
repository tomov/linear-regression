# Multivariable linear regression x => y using gradient descent
#
# Example: gradient_descent([0, 0, 0], 0.01, 1000)
#

import numpy as np

x_1 = [600, 200, 300, 523, 234, 123] # feature 1 samples
x_2 = [3, 2.5, 4, 5, 5, 3] # feature 2 samples
m = len(x_1)
x = np.vstack(([1] * m, x_1, x_2)) # for multi-feature regression

y = [20000, 12000, 14020, 21000, 13210, 11500] # values to predict

assert len(x_1) == len(y)

def h(theta): # [theta_0, theta_1, ...]
    return np.dot(theta, x)

def J(theta):
    return 0.5/m * np.sum((h(theta) - y) ** 2)

def dJ(theta): # dJ / dtheta
    return 1.0/m * np.dot(h(theta) - y, x.T)

def mean_and_range(x):
    a = np.mean(x, axis=1)
    r = np.ptp(x, axis=1) + 1
    return a, r

def mean_and_range_tiled(x):
    a, r = mean_and_range(x)
    a = np.tile(a, (m, 1)).T
    r = np.tile(r, (m, 1)).T
    return a, r

def normalize(x):
    a, r = mean_and_range_tiled(x)
    x = (x - a) / r
    x[0,:] = 1
    return x

def denormalize(x, theta):
    a, r = mean_and_range(x)
    w = np.identity(len(theta)) / r
    w[:,0] = -a / r
    w[0,0] = 1
    return np.dot(theta, w)

def gradient_descent(theta, alpha, steps):
    global x
    x_restore = x
    x = normalize(x)
    print x
    for i in range(steps):
        d = dJ(theta)
        theta -= alpha * d
        j = J(theta)
        print 'Step #{0}: {1} => {2} ({3})'.format(i, theta, j, d)
    x = x_restore
    theta = denormalize(x, theta)
    print theta
    return theta

