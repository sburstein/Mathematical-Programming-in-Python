import random

def rps():
    keep_play = True
    while keep_play:  # You already have a loop so no need to call play() in the function
        human_move = input("Enter Your Move (r for rocks, p for paper, s for scissors): ")
        # You need to validate user input too
        while human_move not in ("r", "p", "s"):
            print("Invalid Input")
            human_move = input(" Please Enter Valid Move (r for rocks, p for paper, s for scissors): ")
        cpu_move = random.choice(("r", "p", "s"))
        # Much clearer than randint
        # Here I use tuples, which are basically lists you can't modify
        # Python will optimize these in certain cases so use them instead of lists for things you never change

        # Defining compare() is useless since you only call it once anyway
        # Comments are only for explanation, if your code is simple to understand try to avoid comments. For example, people can see if you compare to "Rock" that it's the logic for the rock outcomes
        if human_move == cpu_move:
            print("TIE")
        elif human_move == "r" and cpu_move == "p":
            print("You Lose!")
        elif human_move == "r" and cpu_move == "s":
            print("You Win!")
        elif human_move == "p" and cpu_move == "s":
            print("You Lose!")
        elif human_move == "p" and cpu_move == "r":
            print("You Win!")
        elif human_move == "s" and cpu_move == "r":
            print("You Lose!")
        elif human_move == "s" and cpu_move == "p":
            print("You Win!")
        play_again = input("Play again?")
        while play_again not in ("Yes", "No"):  # validate user input
            print("Please try again")
            play_again = input("Play again?")
        if play_again == "No":
            print("Game Over")
            continue_playing = False
        # Don't return here (you returned the input), I really don't think that's what you wanted

def game_start():
    while True:
        begin = input("Would you like to play Rock, Paper, Scissors?")
        if begin == "Yes":
            play()
        elif begin == "No":
            print("Game Over")
        else:
            print("Please try again")
        # No need for return or break here, if-else is enough

if __name__ == "__main__":  # Only run this if run from commandline
    game_start()