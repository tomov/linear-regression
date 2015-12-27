# Linear regression x => y using gradient descent
#
# Example: gradient_descent(0, 0, 0.01, 1000)
#
import numpy as np

x = [600, 200, 300, 523, 234, 123]
m = len(x)

y = [20000, 12000, 14020, 21000, 13210, 11500]

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
