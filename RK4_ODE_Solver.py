
import numpy as np
import matplotlib.pyplot as plt


def ODE_func(r, y):
    """Defining dy/dx function"""
    return r * y * ( 1 - y )

def solution_func(t):
    """Defining given ODE exact solution function"""
    return 1 / ( 1 + np.exp( -t ) )

def predict(r, y0, t0, t1, h = 1e-5):
    """Utilizes RK4 calculation in finding t1"""
    un = y0
    intervals = int(round(abs(t1-t0)/h))
    h=( (t1-t0) / intervals )
    print(intervals)
    print(h)
    for i in range(intervals):
        f1 = ODE_func(r, un)
        f2 = ODE_func(r, un + ((h/2)*f1))
        f3 = ODE_func(r, un + ((h/2)*f2))
        f4 = ODE_func(r, un + (h*f3))
        un += (h/6) * (f1 + (2 * f2) + (2 * f3) + f4)
    return un

def RungeKutta4(r, y0, t0, t1, h = 1e-5):
    """Uses RK4 to generate list of points with step size as optional input"""
    intervals = round( (t1 - t0) / h )
    h = ( (t1-t0) / intervals )
    t = np.linspace(t0, t1, num = intervals + 1)
    u = [0] * (intervals + 1)
    u[0] = y0
    for i in range(1, intervals + 1):
        f1 = ODE_func(r,u[i-1])
        f2 = ODE_func(r,u[i-1]+((h/2)*f1))
        f3 = ODE_func(r,u[i-1]+((h/2)*f2))
        f4 = ODE_func(r,u[i-1]+(h*f3))
        u[i] = u[i-1] + ((h/6)*(f1+(2*f2)+(2*f3)+f4))
    return t, u

def test(r = 1, y0 = 0.5, t0 = 0, t1 = 5, h = 0.2):
    """Test function calls RungeKutta4 with Q1(c) inputs and plots the output along
    with the exact solution. Computed solution is the solid red line, exact:
    solution is the dotted green line. Step size can be adjusted. 0.2 was
    determined to be the largest step size where the solution still looked accurate"""

    t, u = RungeKutta4(r, y0, t0, t1, h)

    plt.figure(1)
    plt.plot(t, u, 'r', label = 'Computed Solution')
    plt.plot(t, solution_func(t), 'g--', label = 'Exact Solution')
    plt.xlabel('t')
    plt.ylabel('y(t)')
    plt.title('Computed and Exact Solutions to Logistic Population Growth ODE')
    plt.legend(frameon = True, loc = 'lower right')
    
def error(r = 1, y0 = 0.5, t0 = 0, t1 = 5, h = 0.2):

    t, u = RungeKutta4(r, y0, t0, t1, h)
    y = [0] * (len(u))
    for i in range(len(u)):
        y[i] = solution_func(t[i])
        u[i] = abs(u[i] - y[i])
    return max(u)

def error_list():
    error_vals = [0] * 10
    x_vals = np.linspace(1, 10, num = 10)
    print(x_vals)
    for k in range(1,11):
        error_vals[k-1] = error(h = (2**(-k)))
    print("errors are {}" .format(error_vals))
    plt.figure(2)
    plt.loglog(x_vals, error_vals)
    plt.xlabel('k')
    plt.ylabel('Error')
    plt.title('Max Error Values of RK4 ODE Solver When h = 2^-k')



if __name__ == "__main__":
    
    error_list()
    test()