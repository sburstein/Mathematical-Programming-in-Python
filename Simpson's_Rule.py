import numpy as np
import matplotlib.pyplot as plt

#By Scott Burstein
"I collaboareted with Sarah Northover on this homework assignment."

def func1(x):
    y = (1 - x**2)**2
    return y

def func2(x):
    y = 1 / (4*((np.sin(2*x))**2) + 1)
    return y


def simp(f, a, b, n): #n is number of points
    h = (b-a)/float(n)
    result = f(a) + f(b)

    for i in range(1,n):
        if i%2 == 0:
            result += 2 * f(a + i*h)
        else:
            result += 4 * f(a + i*h)
    result *= (h/3.0)

    return result

def error_table_1(m):
    """ table of errors for 10^(-1), ... 10^(-n) """

    h = 1
    f = lambda x: (1 - x**2)**2 #func1
    a = 0
    b = 2
    exact = 46/15
    err = 0
    for k in range(m):
        h *= 2
        err = abs(simp(f, a, b, h) - exact)
        ratio = err / (abs(simp(f, a, b, h//2) - exact))
        print(f'{h} \t {err:.1e} \t {ratio}')


def error_plot_1(f, a, b, m): #changed n to m --> maximum exponent
    """ log-log plot of error vs. h for the forward difference"""

    # choose a good density of points, all log-spaced
    nvals = [2**i for i in range(2,m)]
    exact = 46/15
    err = [abs(simp(f, a, b, n) - exact) for n in nvals]

    # plot using pyplot: with and without reference line
  
    plt.figure()
    plt.loglog(nvals, err, '.-k', markersize=12)
    pvals = [n**(-4) for n in nvals]
    plt.loglog(nvals, pvals)
    plt.xlabel('h')
    plt.ylabel('err')
    plt.ylim([1e-12, 1])
    plt.show()

    #p is approximately equal to -4.

def error_table_2(m):
    """ table of errors for 10^(-1), ... 10^(-n) """

    h = 2
    f = lambda x: 1 / (4*((np.sin(2*x))**2) + 1) #func2
    a = 0
    b = np.pi
    exact = 1.404962946208145
    for k in range(m):
        h += 2
        err = abs(simp(f, a, b, h) - exact)
        ratio = err / (abs(simp(f, a, b, h-2) - exact))
        print(f'{h} \t {err:.1e} \t {ratio}')

def error_plot_2(f, a, b, m):
    """ log-log plot of error vs. h for the forward difference"""
    '''
    # choose a good density of points, all log-spaced
    hvals = [4**(-k) for k in range(26) if 4**(-k) > 1e-16]
    x0 = 1
    exact = 1.404962946208145
    err = [abs(simp(f, a, b, n) - exact) for h in hvals]

    # plot using pyplot: with and without reference line
    plt.figure()
    plt.loglog(hvals, err, '.-k', markersize=12)
    
    plt.xlabel('h')
    plt.ylabel('err')
    plt.ylim([1e-12, 1])
    plt.show()
    '''
    
    # choose a good density of points, all log-spaced
    nvals = [i for i in range(2,m,2)]
    exact = 1.404962946208145    
    err = [abs(simp(f, a, b, n) - exact) for n in nvals]

    # plot using pyplot: with and without reference line
  
    plt.figure()
    plt.loglog(nvals, err, '.-k', markersize=12)
    pvals = [n**(-4) for n in nvals]
    plt.loglog(nvals, pvals)
    plt.xlabel('h')
    plt.ylabel('err')
    plt.ylim([1e-12, 1])
    plt.show()

    #for Cn^-p, p is approximately equal to -4.
    


if __name__ == "__main__":

    print(simp(func1, 0, 2, 4)) #
    print(simp(func2, 0, np.pi, 4))

    #print("error table 1:")  
    #error_table_1(7)
    #error_plot_1(func1, 0, 2, 10)
    print("error table 2:")  
    error_table_2(10)
    error_plot_2(func2, 0, np.pi, 50)