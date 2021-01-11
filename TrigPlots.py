
import numpy as np
import matplotlib.pyplot as plt

def trig_func_1(x):
    return np.sin(2*x)

def trig_func_2(x):
    return np.cos(2*x)

if __name__ == '__main__':
    
    x_vals = np.linspace(0, 2 * np.pi, 100)

    sineVals = [trig_func_1(x) for x in x_vals]
    cosineVals = [trig_func_2(x) for x in x_vals]


    plt.figure(figsize=(10, 10))

    plt.plot(x_vals, sineVals, label = 'sin(2x)')
    plt.plot(x_vals, cosineVals, label = 'cos(2x)')

    plt.title('Sine and Cosine Functions')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.legend()
    plt.savefig('TrigPlots.pdf', bbox_inches='tight')
    plt.show()
