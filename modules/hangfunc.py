# Functions that make up the hangman game

import random
import os
from modules import screens

def get_random_word(dict, theme):
    random_word = random.choice(dict["themes"][theme])
    return random_word.upper()

def game(theme, word, score):
    found_letters = ["_" for _ in word] # Transform each letter of the word into "_"
    wrong_letters = []
    attemps = 6
    error = 0
    while attemps > 0:
        os.system("clear || cls")
        print()
        screens.print_its_a_theme(theme)
        print()
        screens.print_hangman(error)
        print()
        print(" ".join(found_letters)) # Display each letter separated by space
        print()
        print("Wrong letters: ", " ".join(wrong_letters))
        print()
        print("Remaining chances:", attemps)
        print()
        while True:
            attemp = input("Get the letter: ").upper()
            if len(attemp) == 1:
                if attemp in wrong_letters:
                    print("You already tried the letter %s before." % attemp)
                    continue
            else:
                print("Type only one letter.")
                continue
            break

        if attemp in word:
            index = 0
            for letter in word:# Loop through all letters
                if attemp == letter: # If the guess (a letter) matches any letter in the word
                    found_letters[index]= letter # Replace the "_" in the word with the corresponding letter
                index += 1 # Prevent the loop from executing at the same index in the next iteration

            if "_" not in found_letters:
                os.system("clear || cls")
                print()
                print(" ".join(found_letters))
                print()
                print("Congratulations! You completed the word!")
                score += 1
                print("Your score is", score)
                print()
                input("<ENTER> to back")
                return score
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
                score -= 1
                print("Your score is", score)
                print()
                input("<ENTER> to back")
                return score