# Functions that make up the hangman game

import random
import os
from modules import screens

def get_random_word(dict, theme):
    random_word = random.choice(dict["themes"][theme])
    return random_word.upper()

def game(word):
    found_letters = ["_" for _ in word]
    wrong_letters = []
    attemps = 6
    error = 0
    while attemps > 0:
        os.system("clear || cls")
        print()
        screens.print_hangman(error)
        print()
        print(" ".join(found_letters))
        print()
        print("Wrong letters: ", " ".join(wrong_letters))
        print()
        print("Remaining chances:", attemps)
        print()
        attemp = input("Get the letter: ").upper()

        if attemp in word:
            index = 0
            for letter in word:
                if attemp == letter:
                    found_letters[index]= letter
                index += 1

            if "_" not in found_letters:
                os.system("clear || cls")
                print()
                print(" ".join(found_letters))
                print()
                print("Congratulations! You completed the word!")
                print()
                input("<ENTER> to back")
                break
        else:
            attemps -= 1
            error += 1
            wrong_letters.append(attemp)
            if attemps == 0:
                os.system("clear || cls")
                print()
                screens.print_hangman(error)
                print()
                print("The word was:", word)
                print()
                print("Too bad, you were 'hanged'! Good luck next time!")
                print()
                input("<ENTER> to back")