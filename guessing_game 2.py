"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""
import sys
import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.

def gameplay():
    
    print("------------------------------------\nWelcome to the Number Guessing Game!\n------------------------------------")

    answer = random.randint(1,15)
            
    try:
        guess = int(input("Please guess a number between 1 and 15: "))
    except ValueError:
        print("Sorry, that is not a valid answer, Please enter a numeral between 1 and 15.")
    else:
        attempt_number = 1
        while guess != answer:
            attempt_number += 1
            if guess < answer:
                try:
                    guess = int(input("Sorry, the number is higher than that, please enter another guess: "))
                except ValueError:
                    print("Please enter an integer(No deimals!) as your numeral.")
            elif guess > answer:
                try:
                    guess = int(input("Sorry, the number is lower than that, please enter another guess: "))
                except ValueError:
                    print("Please enter an integer(No decimals!) as your numeral.")
            else:
                print()
        else:
            print("Congratulations! You got it correct!")
        print("It took you {} attempts.".format(attempt_number))
    
    retry = input("Would you like to play again: (Yes/No)")
    while retry.lower() == "yes":
        gameplay()
    else:
        print("Thank you for playing!\n---------\nGAME OVER\n---------.")
        sys.exit()
            
                          
            
gameplay()
   

    
    
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
