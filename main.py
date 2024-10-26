import json
from modules import screens

opt = ""

while opt != "0":
  opt = screens.menu_select_theme()

  with open("./files/words.json") as archive:
    read = archive.read()
    themes = json.loads(read)