"""
projekt_2.py: Bulls and Cows game
author: Michaela Řežábková
email: rezabkova.michaela@seznam.cz
discord: Míša Ř#8858 
"""

import random
from time import gmtime, mktime


def check_duplicates(num):
    return len(num) == len(set(num))


if __name__ == '__main__':
    print("Hi there!")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("Enter a number:")
    number = str(random.randint(1000, 9999))
    while not check_duplicates(number):
        number = str(random.randint(1000, 9999))
    
    start = gmtime()
    guesscount = 0
    while True:
        guess = input("Enter a number: ")
        guesscount += 1
        if not guess.isnumeric() or len(guess) != 4:
            print("Wrong input, try again.")
            continue
        if not check_duplicates(guess):
            print("Number should not contain duplicates, try again.")
            continue
        bulls = 0
        cows = 0
        for i in range(4):
            if guess[i] == number[i]:
                bulls += 1
            elif guess[i] in number:
                cows += 1
        print(str(bulls)+" bulls, "+str(cows)+" cows")
        if bulls == 4:
            print("Correct, you've guessed the right number")
            break
    time_taken = mktime(gmtime()) - mktime(start)
    result = "It took you "+str(guesscount)+" guesses and "
    result += str(int(time_taken / 60))+" minutes and "+str(int(time_taken % 60))+" seconds"
    print(result)
    print("That's it, you've won")