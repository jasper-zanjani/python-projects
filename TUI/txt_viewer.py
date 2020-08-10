#!/usr/bin/env python
import npyscreen
import sys

filename = 'raven'

class NewMutt(npyscreen.FormMutt):
  def __init__(self, filename):
    super().__init__(self)
    self.wStatus1.value = "The Raven "
    self.wStatus2.value = "by Edgar Allan Poe"
    with open(filename) as f:
      self.wMain.values = [r for r in f]

class App(npyscreen.NPSApp):
  # def onStart(self):
  #   self.addFormClass('MAIN', NewMutt, name='The Raven, by Edgar Allan Poe')
  def main(self):
    # npyscreen.setTheme(npyscreen.Themes.ElegantTheme)
    # npyscreen.setTheme(npyscreen.Themes.ColorfulTheme)
    # npyscreen.setTheme(npyscreen.Themes.DefaultTheme)
    # npyscreen.setTheme(npyscreen.Themes.TransparentThemeDarkText)
    npyscreen.setTheme(npyscreen.Themes.TransparentThemeLightText)

    F = NewMutt(filename)
    F.edit()
    # F.wStatus1.value = "Status Line "
    # F.wStatus2.value = "Second Status Line "
    # with open(filename) as f:
    #   F.wMain.values = [r for r in f]

if __name__ == "__main__":
  try:
    App().run()
  except KeyboardInterrupt:
    sys.exit(0)
