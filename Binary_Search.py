def search(vals, x):

    l_bound = vals[0]
    r_bound = vals[len(vals) - 1]

    if not (x >= l_bound and x <= r_bound):
        return -1

    
    l_index = 0
    r_index = len(vals) - 1

    while r_index - l_index >= 1:
        
        c = (l_index + r_index) // 2 # c is the midpoint index
        Ac = vals[c]

        if x > Ac:
            
            l_index = c + 1
            print( (c+1) , r_index )
            #print("Values: ", vals[c+1], vals[r_index])
            

        elif x < Ac:
            
            r_index = c - 1
            print( l_index , c )
            #print("Values: ", vals[l_index], vals[c])

        
        else: #x = Ac
            return c
            


    if vals[l_index] == x:
        return l_index
    else:
        return -1



if __name__ == "__main__":

    vals = [i for i in range(100)]
    x = 88

    print(search(vals, x))