
"""
Short derivative example - rounding error for a forward difference
-> Version 1: prints a table of the error
-> Version 2: makes a log-log plot (more on this later)
"""
import numpy as np
import matplotlib.pyplot as plt

# Sarah Northover and I collaborated for this part.

def third_der(f, x, h):
    return (f(x + 2*h) -(2*f(x + h)) + 2*f(x - h) - f(x - 2*h))/(2*(h**3))

def fun_q3(x):
    return np.cos(2*x)

def err_table(n):
    """ table of errors for 10^(-1), ... 10^(-n) """

    h = 1
    x0 = 1
    exact = 8*np.sin(2*x0)
    for k in range(n):
        h /= 10
        err = abs(third_der(fun_q3, x0, h) - exact)
        print(f'{h:.1e} \t {err:.1e}')

def err_plot():
    """ log-log plot of error vs. h for the forward difference"""

    # choose a good density of points, all log-spaced
    hvals = [4**(-k) for k in range(26) if 4**(-k) > 1e-16]

    x0 = 1
    exact = 8*np.sin(2*x0)
    err = [np.abs(third_der(fun_q3, x0, h) - exact) for h in hvals]

    # plot using pyplot: with and without reference line
    for j in range(2):
        plt.figure()
        plt.loglog(hvals, err, '.-k', markersize=12)
        if j == 0:  # for comparison (slope 1 on plot), add this to a 2nd ver.
            plt.loglog(hvals, hvals, '--r')
            plt.legend(['err', 'C*h'])

        plt.xlabel('h')
        plt.ylabel('err')
        plt.ylim([1e-12, 1e+20])
        plt.show()


if __name__ == "__main__":
    
    err_table(7)
    err_plot()

"""
Best choice for h is approximately ~= 4.
Minimum error is 3.9e-06 when h is 0.0001.
"""