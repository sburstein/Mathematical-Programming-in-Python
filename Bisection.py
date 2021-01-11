import numpy as np

# ------------------------------
# --------- Code for Q2 --------
# ------------------------------


def find_zero(func, a, b, tol = 1e-12, show = False):
    """ bisection should take in a function f(x) """

    fa = func(a)
    fb = func(b)
    # Note: it's useful to store the f(x) evaluations
    # if you use them more than once, to avoid extra work.
    # you should minimize the # of f(x) evaluations used



    # ... check the initial interval brackets ...
    if not ( (fa < 0 and 0 < fb) or (fa > 0 and 0 > fb) ):
        raise NameError("Function does not cross y-axis in given bounds")

 
    it = 0

    interval_size = (b-a) / 2


    while interval_size > tol:
        c = 0.5*(a + b)
        fc = func(c)

        if fa * fc < 0:
            
            b = c
            fb = fc
            it += 1
            
      
        else: #(if fc * fb < 0)

            a = c
            fa = fc
            it += 1
        
        interval_size = (b-a) / 2

       
        if show == True:
            print(it, ('{:.6f}'.format(c)))
    
    return c, it


def f1(x):  # one of the HW 3 examples
    return x**2 - 9

if __name__ == "__main__":

#Bisection Algorithm (Question 2)


    c = find_zero(f1, 1, 4, tol = 1e-16, show = True)
    #c = find_zero(f1, 2, 4, tol = 1e-16, show = True)
    #c = find_zero(np.sin, 3, 4, 1e-6, show = True)
    #c = find_zero(np.sin, 3, 10, 1e-6, show = True)
    
    #format with fixed num of decimals (also add ---- bars)


    print(c)

    #solution to b
    '''
    In this instance, c = find_zero(f1, 1, 4, tol = 1e-16, show = True)
    Where f1(x) = x**2 - 9
    it takes 21 iterations to get an absolute error that is at most 1 e-6.
    The (it, c) output for this is copied below:
    21 3.0000002384185791
    This output is to 16 digits accuracy.
    '''


    #replacing the print statement on line 50 with
    #print(it, ('{:.16f}'.format(c)))
    #produces output table with 16 floating point decimals rather than 6.

    #solution to c
    '''
    for c = find_zero(f1, 1, 4)
    The approximation's accuracy worsens beyond iteration 52, where the c value = 3.0000000000000000
    this estimate is accurate to all 16 decimal places, the extent of a standard 64-bit computer's processing power.
    Despite this, the algorithm proceeds for another 2 iterations until it = 54, where c = 3.0000000000000009
    The final returned solution tuple in form (c, it) is (3.000000000000001, 54), which is peculiar
    since the 54th iteration output during runtime returned a different c value for that bisection of the interval.
    '''


    #print(f"A floating point number: {c:.6f}, and in sci. notation: {c:.2e}")