import random
import time
"I worked with Sarah Northover on HW5"
# ---------------------------------
# mergesort shell


def built_in_sort(arr):
    arr.sort()
    return arr

def mergesort(arr):
    """ sorts a list of numbers into non-decreasing order."""
    work = [0]*len(arr)
    msort(0, len(arr)-1, arr, work)

def msort(j, k, arr, work):
    """ mergesort - recursive implementation
    What msort is doing:
    array is being partially sorted each time.
    swapping a-b, need temp to store numbers"""

    if j == k:
        return

    elif j == k+1:
        if arr[k] < arr[j]:
            (arr[j], arr[k]) = (arr[k], arr[j]) # flips vals of arr[j] and arr[k] if j is greater than k.

    # divide and sort step
    m = (j+k)//2
    msort(j, m, arr, work)
    msort(m+1, k, arr, work)

    # merge step (you'll need the "work" array)

    lowerDex = j
    upperDex = m+1
    tempDex = j

    while lowerDex <= m and upperDex <= k:
        
        if arr[lowerDex] < arr[upperDex]:
            work[tempDex] = arr[lowerDex]
            lowerDex += 1
        
        else:
            work[tempDex] = arr[upperDex]
            upperDex += 1
        
        tempDex += 1
    
    if lowerDex <= m:
        arr[tempDex : k+1] = arr[lowerDex : m+1]
    
    arr[j : tempDex] = work[j : tempDex]


def test_list(n, maxval=1000):
    """ list of random integers for testing sort """
    random.seed(1)  # fix the random seed, so the list is the same each run.
    return [random.randint(0, maxval) for k in range(n)]

def time_tester(n, num_trials):
    
    sum_comp_times = 0
    sum_msort_times = 0
    
    for trial in range(num_trials):
        num_array = test_list(n, maxval=1000) #seed is specified in test_list (default=1)
        init_comp_time = time.perf_counter()
        built_in_sort(num_array)
        end_comp_time = time.perf_counter()
        sum_comp_times += end_comp_time - init_comp_time
    

        num_array = test_list(n, maxval=1000) #recreate since original is now sorted by comp.
        init_msort_time = time.perf_counter()
        mergesort(num_array)
        end_msort_time = time.perf_counter()
        sum_msort_times += end_msort_time - init_msort_time
    
    avg_comp_time = sum_comp_times / num_trials
    avg_msort_time = sum_msort_times / num_trials

    print("time test for .sort() and mergesort methods")
    print("using " + str(num_trials) + " trials for size " + str(n) + " random array w/ seed specified in test_list()")
    print("-----------------------------")

    print("built-in .sort() method time:")
    print(str(avg_comp_time) + " seconds")
    print("-----------------------------")

    print("recursive mergesort method time:")
    print(str(avg_msort_time) + " seconds")
    print("-----------------------------")

    

if __name__ == '__main__':

    #generate unsorted list of length 4
    unsorted_list = test_list(4)
    print("unsorted list:")
    print(unsorted_list)
    print("---------------------")

    #computer .sort() method
    comp_sort_list =  built_in_sort(unsorted_list)
    print("built-in sort method:")
    print(comp_sort_list)
    print("---------------------")

    #.sort() sorted the unsorted_list. Create again
    second_unsorted_list = test_list(4)
    print("second unsorted list (same as first):")
    print(second_unsorted_list)
    print("---------------------")

    #recursive mergesort() method
    mergesort(second_unsorted_list)
    print("recursive merge sort method returns:")
    print(second_unsorted_list)
    print("---------------------")

    #time trials for both built-in and recursive sorting methods
    print(time_tester(4,20))

    """
    It is evident that the recursive mergesort method (average across 20 trials for array size 4),
    with time 4.7451999999989504e-06 seconds, is appriximately 10 times slower than the built-in .sort()
    method (average across 20 trials for array size 4), with time 5.200499999989672e-07 seconds.
    """

    """
    It is evident that the recursive mergesort method (average across 20 trials for array size 4),
    with time 4.7451999999989504e-06 seconds, is appriximately 10 times slower than the built-in .sort()
    method (average across 20 trials for array size 4), with time 5.200499999989672e-07 seconds.
    """


    """
    Also tested with larger arrays and smaller number of trials. For example, the following output for array size
    1,000,000 and 1 trial:
    ---------------------
    time test for .sort() and mergesort methods
    using 1 trials for size 1000000 random array w/ seed specified in test_list()
    -----------------------------
    built-in .sort() method time:
    0.22975821800000018 seconds
    -----------------------------
    recursive mergesort method time:
    7.336388499 seconds
    -----------------------------
    """

    #Starting with n = 1000 for comparison with 2n, 4n
    #n - n = 1000, trials = 20
    print(time_tester(1000,20))
    #2n - n = 2000, trials = 20
    print(time_tester(2000,20))
    #4n - n = 4000, trials = 20
    print(time_tester(4000,20))

"""
For the built-in .sort() method, time does not increase substantially from n to 2n (~0.00035 sec),
however approximately doubles for 4n test (~0.00058 sec).

Conversely, the recursive mergesort implementation, which is substantially slower than .sort()
for all n sizes, increases at an increasing rate across the three n size trials. 
For 1n: time = 0.008289490550000004 seconds
For 2n: time = 0.011037870600000003 seconds
For 4n: time = 0.017731719999999996 seconds
"""