#power.py code

import numpy as np
from numpy import random
from matplotlib import pyplot as plt

def RayleighQuot(vector):
        return np.sqrt(vector.dot(vector))
    
def AbsMax(vector):
        return np.max(np.abs(vector))

def power_method(a, steps, actualVal):
    """ simple implementation of the power method, using a fixed
        number of steps. Computes the largest eigenvalue and
        associated eigenvector.
        Args:
            a - the (n x n) matrix
            steps - the number of iterations to take
        Returns:
            x, r - the eigenvector/value pair such that a*x = r*x
    """

    #Predefined parameters"
    err_tolerance=1e-10
    max_num_steps = 150

    n = a.shape[0]
    x = random.rand(n)
    it = 0
    error = err_tolerance

    real_error_array = []

    while it < steps and error >= err_tolerance:  # other stopping conditions would go here
        q = np.dot(a, x)  # compute a*x
        r = x.dot(q)    # Rayleigh quotient x_k dot Ax_k / x_k dot x_k

        temp_space = q / RayleighQuot(q)
        error = AbsMax( x - temp_space )

        x[:] = temp_space[:]

        minErrVal = 0

        if AbsMax( x + actualVal ) < AbsMax( x - actualVal ):
            minErrVal = AbsMax( x + actualVal )

        elif AbsMax( x + actualVal ) > AbsMax( x - actualVal ):
            minErrVal = AbsMax( x - actualVal )
        
        else:
            minErrVal = None #Could they ever be equal?

        real_error_array.append(minErrVal)
        it += 1


    return x, r, real_error_array #Return array of real errors


if __name__ == "__main__":   # (3x3 matrix)
    a = np.array([[0.0, 1, 0], [0, 0, 1], [6, -11, 6]])
    # eigenvalues: 3, 2, 1
    # eigenvalues/vectors:
    vector_1 = np.array([1, 3, 9])

    actual_vect1_val = vector_1 / RayleighQuot(vector_1)

    x, r, real_error_array = power_method(a, 100, actual_vect1_val)

    q = np.dot(a, x)
    temp_space = q / RayleighQuot(q)
    error = AbsMax( x - temp_space )

    np.set_printoptions(precision=3)  # set num. of displayed digits

    #print(x,r,real_error_array)

    plt.figure(figsize = (5, 5))
    nvals = range(0, len(real_error_array))
    plt.semilogy(nvals, real_error_array, '.-k')
    reference_line = [(2/3)**n for n in range(5)] #nvals
    plt.semilogy(nvals, ref_line, '--r')
    plt.xlabel('$n$')
    plt.ylabel('err')
    plt.legend(['error in evec', 'slope -2/3'])
    plt.savefig('PowerMethodConvergence.pdf')



    #print(f"Largest eigenvalue: {eig:.2f}")
    #print("Eigenvector: ", evec)