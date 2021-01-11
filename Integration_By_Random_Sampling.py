import random
import math

'''
I collaborated with Sarah Northover on HW 2.
'''

def randPoint(a, b, y_upper):
    
    x = random.uniform(a, b)
    y = random.uniform(0, y_upper)
    coord = (x, y)

    return coord



def randPoint_List(N):
    
    tup_list = [0 for i in range(N)]
    for i in range(N):
        tup_list[i] = (randPoint(a, b, y_upper))

    return tup_list


def half_circle_function(x):
    return (1-(x**2))**0.5

'''
This function graphs the positive (y>=0) portion 
of a circle with radius 1 centered at (0,0).
It's actual integral from x values 0 to 1
= pi/4 which approximates to 0.785398 .
'''

def Monte_Carlo_integration(integrable_function, a, b, y_upper, N):

    N_dist_Points = randPoint_List(N)

    under_curve_count = 0

    for point in N_dist_Points:

        if point[1] <= integrable_function(point[0]):
            under_curve_count += 1   

    under_over_ratio = under_curve_count / (len(N_dist_Points)) # Ratio of points under to total
    rect_area = (b - a) * (y_upper)
    integral_estimate = under_over_ratio * rect_area
    
    return integral_estimate


    
#Error for estimate assumes pi = 3.141592653589793 (16 digits)

def pi_estimate(N):
    pi_est = 4*(Monte_Carlo_integration(half_circle_function, a, b, y_upper, N))
    return pi_est
    

def error_average(N_list, trials):

    err_list = []
    for num_points in N_list:
        pi_est_w_N = pi_estimate(num_points)
        err_sum = 0

        for trial in range(trials):
            err = abs(3.14 - pi_est_w_N)
            err_sum += err

        err_avg = err_sum / trials
    
        err_list.append(err_avg)
        
    return err_list


if __name__ == "__main__":

    a = 0
    b = 1
    y_upper = 1  # Max y for func is 1 @ x=0.
    N = 1000    # N neccessary to get 3.14 consistently is at least 50000+


    #print(pi_estimate(N))

    #print(error_average(N_list, trials))

    trials = 1000
 
    N_list = [i*1000 for i in range(1,11)]
    err_list = error_average(N_list, trials)

    print("Pi Estimation Error based on N Sampling")
    print("Error is average of " + str(trials) + " trials")
    print ("Samples  Error")
    print ("--------------")
    for j in range(1,11):
        print(N_list[j-1], "    "  "{:.2e}".format(err_list[j-1]))
    print ("--------------")



