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