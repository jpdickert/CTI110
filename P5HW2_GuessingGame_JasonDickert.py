# Guessing Game
# 03 July 2018
# CTI-110 P5HW2 - Random Number Guessing Game
# Jason Dickert
#

# generate random number between 1 and 100

import random

def generator():
    number = random.randint(1, 100)
    return number

def inquiry(message = "Guess the number: "):
    guess = int(input(message))
    return guess

def feedback(guess, number):
    if guess > number:
        return "The number is too high."
    elif guess < number:
        return "The number is too low."
    else:
        return "You guessed the number!"

def main():
    won = False
    while won == False:
        number = generator()
        guess = inquiry()
        message = feedback(guess, number)

        while message != "You guessed the number!":
            print(message)
            guess = inquiry("Try again: ")
            message = feedback(guess, number)

        while message == "You guessed the number!":
            play_again = input("You guessed the number! Play again? Enter 'Y' for yes: ")
            won = True
        if play_again == "y" or play_again == "Y":
            won = False

        
main()
