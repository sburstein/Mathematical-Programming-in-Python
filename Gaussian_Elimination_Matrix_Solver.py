""" shell for HW 3 problems.
    Note that you should replace my placeholder
    doc-strings with actual descriptive ones.
"""
import numpy as np


# ----------------------------------
# ---- Code for Q1a, Q1b, Q1c ------
# ----------------------------------

#Assumes row major matrices for all

def fwd_solve(a, b):
    n = len(b)
    x = [0]*n
    for i in range(n):
        x[i] = b[i]
        for j in range(i):
            x[i] -= a[i][j] * x[j]
        x[i] /= a[i][i]
    
    return x

def back_solve(a, b):
    """ backward substitution, returning a new list """
    n = len(b)
    x = [0]*n
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= a[i][j] * x[j]
        x[i] /= a[i][i]

    return x


def residual(a, x, b):
    """ Calculates the residual A*x - b, returning a new list """
    n = len(b)
    res = [0]*n
    Ax = [0]*n   #could I just use Ax = 0? Tradeoffs w/ processing speed
    for i in range(n):
        for j in range(n):
            Ax[i] += x[j] * a[i][j]
        res[i] = Ax[i] - b[i] #should this be abs() ?

    return res


def error_example():
    """ Solves Hx = b using Gaussian elim (with numpy's implementation),
        for a problem where the exact solution is also given.
    """
    # create the matrix and RHS for Hx = b
    n = 6
    hilb = [[1/(j + k + 1) for k in range(n)] for j in range(n)]
    b = [6, 617/140, 499/140, 2531/840, 1649/630, 12847/5544]

    x_comp = np.linalg.solve(hilb, b).tolist()  # computed solution
    x_true = [1, 2, 3, 4, 5, 6]  # true solution

    # calculate the error between x_comp and x_true...
    error = [0]*n
    for k in range(n):
        error[k] = abs(x_comp[k] - x_true[k])
    max_error = max(error)

    # calculate the residual for x_comp...
    
    res_x_comp = residual(hilb, x_comp, b)
    abs_res_x_comp = [abs(k) for k in res_x_comp]
    max_abs_res_x_comp = max(abs_res_x_comp)

    # compare the max. absolute value of components for each
    # (so you should end up comparing *two numbers*)
    print("-------------------------------")
    print("Comparison of Max. Abs. Values")
    print("Between x_comp and x_true")
    print("-------------------------------")
    print("Error \t \t Residual")
    print("{:.2e}".format(max_error) + "\t " + "{:.2e}".format(max_abs_res_x_comp))
    print("-------------------------------")



if __name__ == "__main__":

#Gaussian Elimination Error Example (Question 1)
    error_example()

'''
The expected output is:

-------------------------------
Comparison of Max. Abs. Values
Between x_comp and x_true
-------------------------------
Error            Residual
9.54e-10         4.44e-16
-------------------------------

This indicates that the Error for  Numpy's linear algebra matrix solver,
when applied to the Hilbert Matrix, produced an error = 9.54e-10 ,
which is considered large.

The residual, on the other hand, was quite precise.
residual = 4.44e-16, which is 2*(machine epsilon).

A residual is a helpful estimation for a Matrix solver's accuracy
when the solution is unknown.
'''


