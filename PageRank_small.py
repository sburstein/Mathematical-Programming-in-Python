# Lecture code: bee example.
# The power method for computing a stationary distribution,
# plus code for choosing a move from a state to the next.
#
# Also: pagerank example from class (with four nodes)

import numpy as np
from numpy.random import uniform, rand   # for a random number

def RayleighQuot(vector):
        return np.sqrt(vector.dot(vector))
    
def AbsMax(vector):
        return np.max(np.abs(vector))

# --------------------------------------------------------
# Stationary distribution calculation from theory
def stationary(pt, steps, tolerance = 1e-8):
    """Power method to find stationary distribution.
       Given the largest eigenvalue is 1, finds the eigenvector.
    """
    x = rand(pt.shape[0])  # random initial vector
    x /= sum(x)
    error = tolerance
    for it in range(1, steps+1):
        if error > tolerance:
            temp = np.dot(pt, x)
            x[:] = temp[:] #deep copy
            error = AbsMax(x - temp)
    return x, it


# --------------------------------------------------------
# Pagerank example from lecture

def pagerank_small(alpha = 0.9, num_iters = 100):
    """ small pagerank example from lecture (four nodes) """
    
    n = 4

    p_matrix = np.array([
                         [0,   1/2,  0,  1/2],
                         [0,    0,   1,    0],
                         [1/3, 1/3,  0,  1/3],
                         [0,    0,   1,    0]
                        ])

    # not efficient here; just to illustrate calculation
    pt_mod = np.zeros((n, n))
    for j in range(n):
        for k in range(n):
            pt_mod[j, k] = alpha*p_matrix[k, j] + (1-alpha)*(1/n)

    # NOTE: you can shorthand this with
    # pt_mod = alpha*p_matrix.transpose() + (1-alpha)/n
    # which uses numpy's rules for adding scalars to arrays
    # For efficient code, you'd construct the transpose directly

    dist, steps = stationary(pt_mod, num_iters)


    print("Sites:        ", [str(i) + "      " for i in range(1,n+1)])
    print("Distribution: ", dist)
    print("# of Steps: ", steps)

if __name__ == "__main__":

    #pagerank_small()

    #pagerank_small(0.95)
    """
    When n = 4 and num_iters = 100, 
    pagerank_small(0.95) distribution varies from run to run significantly.
    Common Values were around 
    Distribution:  [0.3184117  0.06998904 0.33641514 0.27518412]
    """

    pagerank_small(alpha = 0.95, num_iters = 1000000)

    """
    Increasing the number of iterations does not really impact the accuracy 
    or consistency of trials. For example, with very large num_iters,
    (1,000,000), the Distribution still varies siginficantly:
    Distribution:  [0.02050526 0.53461778 0.27786379 0.16701316]
    Distribution:  [0.44357702 0.05746809 0.33560291 0.16335198]

    This is concerning, given that the number of iterations does not 
    change the system's accuracy. 
    """

    pagerank_small(alpha = 0.80, num_iters = 100)

    """
    It is difficult to determine whether this is the threshold, 
    but the page rankings definitely change when alpha = 0.8 .
    From different trials, distributions change the page ranking

    Sites:         ['1      ', '2      ', '3      ', '4      ']
    Distribution:  [0.30829037 0.06009597 0.51205546 0.1195582 ] --> Page 3 
    Distribution:  [0.26321444 0.58679477 0.02766653 0.12232427] --> Page 2
    Distribution:  [0.35557852 0.23354842 0.01352491 0.39734815] --> Page 4
    # of Steps:  100

    """

    """
    It seems as though my pagerank is too volatile with changing alpha 
    and not responsive enough with varying number of steps.
    """