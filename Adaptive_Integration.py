import numpy as np

#By Scott Burstein
#Exact integral value is ~2.1

def func3(x):
    y = 5 * ( np.e ** (-50*x) ) + np.sin(x)
    return y


def simp(f, a, b, n):
    h = (b-a)/float(n)
    result = f(a) + f(b)

    for i in range(1,n):
        if i%2 == 0:
            result += 2 * f(a + i*h)
        else:
            result += 4 * f(a + i*h)
    result *= (h/3.0)

    return result

def error_table_3(m):
    """ table of errors for 10^(-1), ... 10^(-n) """

    h = 1
    f = lambda x: 5*(np.e**(-50*x)) + np.sin(x) #func3
    a = 0
    b = np.pi
    exact = 2.1
    err = 0
    
    print("n        error           interval size           error ratio")
    for k in range(m):
        h *= 2 #(b-a)/float(m)
        interval_size = (b-a)/float(h)
        err = abs(simp(f, a, b, h) - exact)
        ratio = err / (abs(simp(f, a, b, h // 2) - exact))
        print(f'{h} \t {err:.1e} \t {interval_size} \t {ratio}')


if __name__ == "__main__":

    print(simp(func3, 0, np.pi, 10))
    #print(simp(func2, 0, np.pi, 4))
    print("error table 3:")  
    error_table_3(10)
    