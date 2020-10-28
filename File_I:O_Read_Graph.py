"""
File I/O example
@author: jtwong
"""
import numpy as np

#Python list used for adjacency matrix. Sarah Northover and I collaborated.

def read_graph_data(fname):

    adj = {}
    names = {}

    fp = open(fname, 'r')

    node_prefix = 'n'
    edge_prefix = 'e'

    for line in fp:

        comps = line.split(' ')
        
        index = int(comps[1])
        
        if comps[0][0] == node_prefix: #Data entry represents Node
            val = comps[2].strip('\n')
            names[index] = val
        
        elif comps[0][0] == edge_prefix: #Data entry represents Edge
            name = int(comps[2])
            if index not in adj:
                adj[index] = [name]
            else:
                adj[index].append(name)

    return adj, names


if __name__ == "__main__":  

    adj_output, names_output = read_graph_data("graph.txt")

    print('adj:  ', adj_output, '\nnames:', names_output)

    #OUPUT:
    """
    adj: {0: [1, 3], 1: [2], 2: [1, 0]} 
    names: {0: 'A', 1: 'B', 2: 'C', 3: 'D'}
    """