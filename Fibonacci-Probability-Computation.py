# For Exercise 1
def build_player_data():
    """ Creates name/player num/batting averages lists
        for an example team.
    """
    names = ["Gunther O'Brian",
             'Workman Gloom',
             'Esme Ramsey',
             'Cornelius Games',
             'Kline Greenlemon',
             'Hotbox Sato',
             'Famous Owens',
             'Jenkins Good']
    nums = [77, 31, 37, 6, 14, 53, 7, 64]
    avgs = [0.40666, 0.118451, 0.400093, 0.335117,
            0.425694, 0.353378, 0.179842, 0.246856]

    return names, nums, avgs


def print_avg():
    """ prints batting averages for the example team """


# For P1
def prob_list(n, p):

    """This function calculates q-n values by
    constructing a list of q values starting from 
    q-0 up to q-n, and returning the last one"""
    ...
#pn is the probability of seeing a pair of aces two hands in a row in n hands.
#qn = 1 - pn
#thus qn is the probability of NOT seeing a par of aces two hands in a row in n hands.
    list = []
    qn_a = 1
    qn_b = 1
    list.append(qn_a)
    list.append(qn_b)

    for i in range(n-2):
        i += 0
        qn_next = (1-p)*qn_b + p*(1-p)*qn_a
        list.append(qn_next)
        qn_a = qn_b
        qn_b = qn_next
    return list


    # returns list of probs. [q0,... qn]

def prob(n, p):
    qn_a = 1
    qn_b = 1
    for k in range(n-2):
        qn_c = (1-p)*qn_b + p*(1-p)*qn_a
        qn_a = qn_b
        qn_b = qn_c

    return qn_c  # return only final qn (without using list)

def n_finder(qn,p):
    
    n=3
    while prob(n,p) > 0.5:
        
        n += 1
        if n%100 == 0: #this prints n integer and associated probability p every 100 n values so user can view algorithm's progress.
            print(n) 
            print(prob(n,p))

    return n

    #n_finder returns n necessary to reach a set qn parameter.



# For P2

from random import randint


def cpu_move(moves_list):
    """returns the move taken by the computer,
    given a list of previous moves."""
    
    move = randint(0,3)
    return move

# Note that you can modify this to take in
# two lists (of player/cpu moves) instead.

def rps():
    """ plays games of rock-paper scissors,
        then summarizes the results.
    """
    # do stuff to initialize
    moves_list = []
    result = []
    
    play = True
    while play:
        
        human = int(input("Enter Your Move (0 for rocks, 1 for paper, 2 for scissors): "))
        while human not in [0,1,2]:
            human = int(input("Enter a valid input (0 for rocks, 1 for paper, 2 for scissors): "))
        
    
        #should cpu_move go here?
        comp_int = cpu_move(moves_list)
        #comp_int = randint(0,3)

        moves_list.append([human,comp_int])


        if human == 0: #human chooses rock
            if comp_int == 0:
                #tie
                result.append("T")
                print(str([human,comp_int]) + "Both choose rock. Tie!")
            elif comp_int == 1:
                #comp wins paper v. rock
                result.append(0)
                print(str([human,comp_int]) + "CPU wins paper over rock!")
            else:
                #human wins rock v. scissor
                result.append(1)
                print(str([human,comp_int]) + "you win rock over scissor!")
        
        elif human == 1: #human chooses paper
            if comp_int == 0:
                #human wins paper v. rock
                result.append(1)
                print(str([human,comp_int]) + "you win paper over rock!")
            elif comp_int == 1:
                #tie
                result.append("T")
                print(str([human,comp_int]) + "Both choose paper. Tie!")
            else:
                #comp wins scissor v. paper
                result.append(0)
                print(str([human,comp_int]) + "CPU wins scissor over paper!")
        
        else: #human chooses scissor
            if comp_int == 0:
                #comp wins rock v. scissor
                result.append(0)
                print(str([human,comp_int]) + "CPU wins rock over scissor!")
            elif comp_int == 1:
                #human wins scissor v. paper
                result.append(1)
                print(str([human,comp_int]) + "you win scissor over paper!")
            else:
                #tie
                result.append("T")
                print(str([human,comp_int]) + "Both choose scissor. Tie!")
        


        keep_play = input("Want to play again? (y/n): ")
        if keep_play == "y":
            play = True
        if keep_play == "n":
            play = False
 
    # summarize the results
    sumout = ""
    sumout += "player cpu \n"
    sumout += "----------- \n"
    for k in range(len(moves_list)):
        sumout += str(moves_list[k]) + " " + str(result[k]) + "\n"
    pct = (result.count(1)/(result.count(1) + result.count(0)))*100
    
    if pct > 50:
        sumout += "winner: player! \n"
    elif pct == 50:
        sumout += "Tie! \n"
    else:
        sumout += "winner: CPU! \n"

    sumout += "win pct: {:.2f} \n".format(pct)

    print(sumout)


if __name__ == "__main__":

    p = (4/52)*(3/51)

    print(prob_list(10,p))
    print(prob(10,p))
   
    "estimate for n such that number of pairs-in-a-row is 1 if n = 1/(a^2) = 48841"
    print(1/(p**2))

    "Determine n computationally such that qn <= 0.5"
    print(n_finder(0.5,p))

    "confirm n_finder results by running n value in prob(n,1) function. It works!"
    print(prob(34009,p))

    "Hence, 34009 hands must be played to have at least a 50% chance of two pairs of aces in a row."


    rps()