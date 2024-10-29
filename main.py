import json
from modules import screens, hangfunc

opt = ""

while opt != "0":
  opt = screens.menu_select_theme()

  with open("./files/words.json") as archive:
    read = archive.read()
    themes = json.loads(read)

    if opt == "1":
      theme = "Animals"
      word = hangfunc.get_random_word(themes, theme)
      hangfunc.game(word)