import random

def get_random_word(dict, theme):
    random_word = random.choice(dict["themes"][theme])
    return random_word.upper()