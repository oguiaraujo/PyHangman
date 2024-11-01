# Screens

import os

def menu_select_theme():
  os.system("clear || cls")
  print()
  print("╔═══════-PYHANGMAN-═══════╗")
  print("║                         ║")
  print("║     1. ANIMALS          ║")
  print("║     2. COUNTRIES        ║")
  print("║     3. FOODS            ║")
  print("║     4. MOVIES           ║")
  print("║     0. EXIT             ║")
  print("║                         ║")
  print("╚═════════════════════════╝")
  opt = input("    Choose an option: ")
  return opt

def print_hangman(error):
  if error == 0:
    print("  +---+  ")
    print("      |  ")
    print("      |  ")
    print("      |  ")
    print("      |  ")
    print("     === ")

  elif error == 1:
    print("  +---+  ")
    print("  O   |  ")
    print("      |  ")
    print("      |  ")
    print("      |  ")
    print("     === ")

  elif error == 2:
    print("  +---+  ")
    print("  O   |  ")
    print("  |   |  ")
    print("      |  ")
    print("      |  ")
    print("     === ")

  elif error == 3:
    print("  +---+  ")
    print("  O   |  ")
    print(" /|   |  ")
    print("      |  ")
    print("      |  ")
    print("     === ")

  elif error == 4:
    print("  +---+  ")
    print("  O   |  ")
    print(" /|\\  |  ")
    print("      |  ")
    print("      |  ")
    print("     === ")

  elif error == 5:
    print("  +---+  ")
    print("  O   |  ")
    print(" /|\\  |  ")
    print(" /    |  ")
    print("      |  ")
    print("     === ")

  elif error == 6:
    print("  +---+  ")
    print("  O   |  ")
    print(" /|\\  |  ")
    print(" / \\  |  ")
    print("      |  ")
    print("     === ")