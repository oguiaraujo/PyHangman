# Imports header
import json
from modules import screens, hangfunc

#╔═══════-PYHANGMAN-═══════╗
#║                         ║
#║     PyHangman v1.2      ║
#║                         ║
#║  A classic hangman game ║
#║  developed in Python,   ║
#║  showcasing skills in   ║
#║  JSON file handling.    ║
#║                         ║
#║  Author: José Guilherme ║
#║  Silva de Araújo        ║
#║                         ║
#║  Educational Project    ║
#║  Data Science Academy   ║
#║                         ║
#╚═════════════════════════╝

opt = ""
while opt != "0":
  opt = screens.menu_select_theme()
  # Read the JSON file
  with open("./files/words.json") as archive:
    read = archive.read()
    themes = json.loads(read)

    if opt == "1":
      theme = "Animals" # Define the theme corresponding to the option
      word = hangfunc.get_random_word(themes, theme) # Store the result of the word draw according to the theme
      hangfunc.game(word) # Run the game based on the selected word

    if opt == "2":
      theme = "Countries"
      word = hangfunc.get_random_word(themes, theme)
      hangfunc.game(word)

    if opt == "3":
      theme = "Foods"
      word = hangfunc.get_random_word(themes, theme)
      hangfunc.game(word)

    if opt == "4":
      theme = "Movies"
      word = hangfunc.get_random_word(themes, theme)
      hangfunc.game(word)