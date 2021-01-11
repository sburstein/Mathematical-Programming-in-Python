"""

Scott Burstein
Math 260 Challenge Problems

Problem 1: Rat Test! (w/ tuple implementation)
Problem 2: Toeplitz Matrix Construction
Problem 3: Chain Class (i.e. linked list construction using classes)
"""

import random  # for random.uniform(a,b) or random.randint(a,b)
# *no other imports* should be used

# ---------------------------------------------
# PROBLEM 1: rats!
def scurry(n, start, minutes, show = False):

    position = start
    time_pos_tuple_list = []
    for time in range(minutes): #Starting position at t = 0, then n movements = number of minutes (minutes+1??)
        time_pos_tuple_list.append((time , position))

        if position == 0:
            next_position = random.randint(position, position + 1) #P = 0.5 each
            position = next_position
        elif position == n-1:
            next_position = random.randint(position - 1, position) #P = 0.5 each
            position = next_position
        else:
            next_position = random.randint(position - 1, position + 1) #P = 0.33 each
            position = next_position
        #print(time, position)
    
    if show == True:
        print("time room")
        for tup in time_pos_tuple_list:
            print(str(tup[0]) + "    " + str(tup[1]))

    
    return position


def distribution(n, start, minutes, num_trials = 1000):
    rat_pos_dict = {}
    for trial in range(num_trials):
        rat_pos = scurry(n, start, minutes)

        if rat_pos not in rat_pos_dict:
            rat_pos_dict[rat_pos] = 0
        rat_pos_dict[rat_pos] += 1

    
    ret_list = []
    for entry in rat_pos_dict:
        room = entry
        prop = rat_pos_dict[room] / num_trials
        tup = (room, prop)
        ret_list.append(tup)
    ret_list.sort()
    
    return ret_list  # return list of probabilities


# (put written answer here)
def rat_test():
    n = 9
    
    # code for the example in M1b

"Answers below in __main__ "

# ---------------------------------------------
# PROBLEM 2: toeplitz matrix construction

def toeplitz(vals):
    
    n = int((len(vals) - 1) / 2)  # (n x n matrix)
    matrix = [ [ 0 for k in range(n+1) ] for j in range(n+1) ]

    for row in range(n, -1, -1):
        for col in range(n, -1, -1):
            matrix[row][col] = vals[n - row + col]
 
    return matrix

def mat_test():
    """ test for M2: given example """
    vals = [1, 4, 9, 16, 25]
    mat = toeplitz(vals)
    print(mat)


# ---------------------------------------------
# PROBLEM 3: Chain class
class Node:
    """ Node class for the Chain, with data and a link to a next Node """

    def __init__(self, data, right):
        """ constructor: right is a *Node*; you can assume data is an int """
        self.data = data
        self.right = right

    def __repr__(self):
        return "N(" + str(self.data) + ")"


class Chain:

    def __init__(self, data = None): #changed data preset to None
        self.data = data
        self.base = None

    def __repr__(self):
        result = "C(" + str(self.data) + ")"

        return result  # returns a string

    def pop(self):
        
        pop_node = self.base
        self.base = self.base.right

        return pop_node  # return data in the popped node
        
        #Assumed to be O(N) time complexity

    def prepend(self, data):
        
        new_base_node = Node(data, None)
        new_base_node.right = self.base
        self.base = new_base_node

        #Assumed to be O(N) time complexity

    def insert(self, data, k):
        
        if self.base == None:
            raise Exception("Chain is empty")
        for node in self:
            if node.right == k: #node.right for k-1 node depends on naming convention?
                data.right = node.right
                node.right = data

        #if k not found in chain....
        raise Exception("k index out of bounds (too large) Error")


    def attach(self, more):  # more is a Chain
        if more is None:
            return self

        self.right = attach(self.right, more)
        return self

    #I tried using recursion!

    #Another method I could have used...
    """
        while more is not None:  
            self.right = more
            more = more.right
    """
        # (no return)


def squares(n):  # create the 1 - 4 - 9 - ... chain
    
    ret_chain = [str(i**2) for i in range(1,n+1)]
    return ret_chain   # return the Chain

    """
    This will be slower than simply traversing 
    through the chain with class methods.
    """

#Would subsequently attempt to implement the method this way:

    """    
    last_node = Node(n, None)
    values = []
    for i in range(n-1, 0, -1):
        str(node)+str(i) = Node(i++2, str(node)+str(i+1))
        values.insert(0, str(node)+str(i))

    squares_chain = Chain(values)
    """




if __name__ == "__main__":
    
# ---------- Question 1 --------------------------  
    print("----- Question 1 ---------------------------")    
    rat_test = scurry(5, 0, 10, show=True)
    print(rat_test)


    #distribution(n, start, minutes, num_trials = 1000)
    
    print("Distribution starting in leftmost room:")
    print(distribution(9,0,60))

    """
    The probability that the rat is is in room 0 
    when starting in room 0 (leftmost) is 0.094 .
    """

    print("Distribution starting in rightmost room:")
    print(distribution(9,8,60))

    """
    The probability that the rat is is in room 0 
    when starting in room 8 (rightmost) is 0.072 .
    """    

# ---------- Question 2 --------------------------  
    print("----- Question 2 ---------------------------")   
    mat_test()
    
    
# ---------- Question 3 --------------------------   
    print("----- Question 3 ---------------------------")
    c = Chain('data') #chain with 1 node having value data
    print(c)


    test_list = Chain()
    test_list.base = Node(3, None)
    print(test_list.base.data)

    node3 = Node(3, None)
    node2 = Node(2, node3)
    node1 = Node(1, node2)



    