def collatz(s):
    """ Computes the Collatz sequence starting at s. """
    ...

    num_list = []

    num_list.append(s)

    while s > 1:
        if s%2 == 0:
            new_s = int(s/2)
            num_list.append(new_s)
            s = new_s
        else:
            new_s = int((3*s)+1)
            num_list.append(new_s)
            s = new_s
    
    return(num_list)


if __name__ == "__main__":
   
   start = 45
   col = collatz(start)

   print("Sequence starting with {}...".format(start))

   for num in collatz(start):
       print(num)

   print("Length = {}".format(len(collatz(start))))
   
   