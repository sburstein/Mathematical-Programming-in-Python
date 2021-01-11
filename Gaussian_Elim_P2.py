"Scott Burstein Gaussian Elimination Matrix Solver Part 2"

import numpy as np


def fwd_solve(a, b):
    """ fwd. substition for Lx = b,
        returning a new vector x with the solution.
    """
    n = len(b)
    x = [0]*n
    for i in range(n):
        x[i] = b[i]
        for j in range(i):
            x[i] -= a[i][j]*x[j]
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

#I collaborated with Sarah Northover on ge_lu function.

def ge_lu(a):
    """ LU factorization of the matrix a. Returns L and U in one matrix. """
    n = len(a)
    #print(n)
    mat = [row[:] for row in a]  # make a copy of a


    pivot_element = [i for i in range(n)]
    

    for k in range(n-1):
        # reduce k-th column
        
        # with pivoting: choose the pivot element,
        # swap rows and update permutation vector.

        elems = [0]*n
        for x in range(k, n):
            elems[x] = abs(mat[x][k])

 
    
        max_index = elems.index(max(elems))
        temp_val = pivot_element[k]
        pivot_element[k] = pivot_element[max_index]
        pivot_element[max_index] = temp_val  # reduce k-th column


        temp_val = mat[k]
        mat[k] = mat[max_index]
        mat[max_index] = temp_val
        

        for i in range(k+1, n):
            # zero out (i, k) entry
            mat[i][k] /= mat[k][k]
            
            for j in range(k+1, n):  # row reduction for i-th row
                mat[i][j] -= mat[i][k] * mat[k][j]
                # update entry in row

    return mat


''' 
Other attempted approach which did not work using list comp. for elems and np.argmax

    for k in range(n-1):
        elems = [0]*n

        elems = [abs(a[j][k]) for j in range(k, n)]
        row_index_max = np.argmax(elems) + k

        np.argmax(abs(A[k:n,k])) + k
        
        pivot_element[[k, row_index_max]] = pivot_element[[row_index_max, k]]
        a[[k, row_index_max]] = a[[row_index_max, k]]


        for y in range(j):
            for x in range(k):
                elems.append(mat[x][y])
'''

# Template for version without pivoting

def linsolve(a, b):
    """ 
    linsolve(a, b) is a function that solves equation for 
    matrices ax = b, where b is a column of values
    and returns the solution. It processes the result
    by using the ge_lu(), fwd_solve(), and back_solve() helper functions.
    """
    n = len(b)
    x = [0]*n
    y = [0]*n  # optional: change code to avoid need for this intermediate vec.

    mat = ge_lu(a)
    y = fwd_solve(mat, b)
    x = back_solve(mat, y)
    return x


# Template for version with pivoting
'''
def linsolve(a, b):
    """ put a doc-string here describing the algorithm """
    n = len(b)
    x = [0]*n
    y = [0]*n  # optional: change code to avoid need for this intermediate vec.

    mat, p = ge_lu(a)
    y = fwd_solve(mat, b, p)  # OR compute pb = P*b, then fwd_solve(mat, pb)
    x = back_solve(mat, y)
    return x
'''


def residual(a, x, b, abs_tf = True):
    """ Calculates the residual A*x - b, returning a new list """
    n = len(b)
    res = [0]*n
    Ax = [0]*n
    for i in range(n):
        for j in range(n):
            Ax[i] += x[j] * a[i][j]

            if abs_tf:
                res[i] = abs(Ax[i] - b[i])
            else:
                res[i] = Ax[i] - b[i]

    return res

 

 

def error_test(a, b):

    """ Calculates x and the residual, printing

    both.

    """

 

    x_comp = linsolve(a, b)  # computed solution

 

    # calculate the residual for x_comp

    res = residual(a, x_comp, b)
    print(res)

 

    max_res = max(res)

    print("x was calculated as:\n", x_comp, "\n")

    print('Maximum Residual')

    print("-------------------")

    print('{:.5e}'.format(max_res))

 


if __name__ == "__main__":

    # typical structure of linsolve call:
    '''
    a = [[1,0,0], [0,1,0], [0,0,1]]
    b = [1,2,3]
    x = linsolve(a, b)
    print(x)
    '''
    
    
    # testable 4x4 Matrix

    a = [
    [0,3,2,1], 
    [4,0,7,5],
    [8,2,0,2],
    [0,1,2,0]
    ]

    b = [
        -3,
         2,
        -2,
        -5
        ]

    
    x = linsolve(a, b)
    print(x)

#testing ax-b

    error_test(a, b)

    '''
    There is a maximum residual between the linsolve() method 
    and the computed solution for this ax-b computation of 5.00000e+00.
    This seems unlikely, as the linsolve() method is proposed to be much more accurate.
    There should not be an error of ~5 for the linsolve - computed methods.
    Further testing will need to be done in order to determine issue.
    '''


    