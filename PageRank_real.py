
import numpy as np

def power_method_ranking(mat, steps = 100):
    """ simple implementation of the power method, using variable
        number of steps. Computes eigenvector.
        Args:
            mat - the (n x n) matrix
            steps - the number of iterations to take
        Returns:
            x - the eigenvector such that a*x = r*x
    """
    n = mat.shape[0]
    x = np.random.rand(n)
    x /= sum(x)
    for it in range(steps): 
        x = np.dot(mat, x)  # compute a*x
        x /= sum(x)
    return x


def sparse_rank(mat, telep, steps = 150):
    """ Sparse Matrix Power method for pagerank
        Args:
            mat - transpose of the transition matrix (P^T)
            telep - the teleport parameter (also known as alpha)
            steps - the number of steps to take (default = 150)
        Returns:
            x - page rank output
    """
    n = mat.shape[0]
    x = np.random.rand(n)
    x /= sum(x)
    for it in range(steps):
        x = telep * mat.dot(x)
        x += (1 - telep) / n
        x /= sum(x)
    return x


# read_graph_file func taken from jtwong1 hw7_soln_partial.py

# file IO

def read_graph_file(fname, node_pre='n', adj_pre='a', edge_pre='e'):
    """ First, it reads lines with prefix n (for node) of the form
        n k name    and stores a dict. of names for the nodes.
        Reads adj. matrix data from a file, returning the adj. list.
        Format: A line starting with...
            - 'n' is read as  n k name  (the node's name)
            - 'e' is read as e k m (an edge k->m)
        Returns:
            adj - the adj. dictionary, with adj[k] -> list of neighbors of k
            names - the dictionary of node names, if they exist
        NOTE: the adj. list does not store dead nodes (with no links)
    """
    adj = {}
    names = {}

    with open(fname, 'r') as fp:
        for line in fp:
            parts = line.split(' ')
            if len(parts) < 2:
                continue
            node = int(parts[1])
            if parts and parts[0][0] == 'n':
                names[node] = parts[2].strip('\n')
            elif parts and parts[0][0] == 'e':
                v = int(parts[2])
                if node not in adj:
                    adj[node] = [v]
                else:
                    adj[node].append(v)

    return adj, names



if __name__ == "__main__":

    adj_dict, names_dict = read_graph_file('california.txt')
    name_length = len(names_dict)
    PT_matrix = power_method_ranking(adj_dict, name_length)
    sparse_matrix = sparse_rank(PT_matrix, 0.99, steps = 500)

    all_tups = zip(names_dict.values(), sparse_matrix)
    tup_list = []
    for page, rank in all_tups:
        tup = (page, rank)
        tup_list.append(tup)
    tup_list.sort(key = lambda x : x[1], reverse = True)

    for num in range(1,11):
        print( str(num) + "     " + str(tup_list[num]) )