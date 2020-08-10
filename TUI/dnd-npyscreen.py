# Implement Picker class to abstract the various pickers

import npyscreen
import sys
from enum import Enum

class Picker(npyscreen.Form):
  def create(self, title: str, desc_text: str , values : list, next_form : str = None ):
    self.add(
      npyscreen.FixedText,
      value = title
    )
  def afterEdition(self):
    self.parentApp.setNextForm()

class RacePicker(npyscreen.Form):
  def create(self):
    self.add(
      npyscreen.FixedText,
      value = 'This is where you choose your character\'s race, which can affect many other statistics...' )
    
    self.nextrely += 1 # Move the next widget on the form further down
    
    # self.random = self.add(
    #   npyscreen.SelectOne,
    #   name = 'Choose randomly',
    #   values = ['Random']
    # )
    
    self.nextrely += 1

    self.selection = self.add(
      npyscreen.SelectOne,
      name = 'Choose the race of your character',
      scroll_exit = True,
      values = race_desc )
  def afterEditing(self):
    self.parentApp.setNextForm('CLASS')

class ClassPicker(npyscreen.Form):
  def create(self):
    self.selection = self.add(
      npyscreen.SelectOne,
      name = 'Choose the class of your chracter',
      scroll_exit = True,
      values = class_desc,
    )
  def afterEditing(self):
    self.parentApp.setNextForm(None)

race_desc = [
  "Dwarf              - Bold, hardy, warrior, miner, long memory and grudges",
  "Mountain Dwarf     - Strong, hardy, rugged, tall for a dwarf",
  "Hill Dwarf         - Keen senses, deep intuition, remarkable resilience",
  "Elf                - Magical people of otherworldly grace, in but not of the world",
  "Wood Elf           - Keen senses and intuition, fleet feet, and stealth",
  "High Elf           - Keen mind and master of basic magic",
  "Drow               - Follow the god Lolth down the path of evil and corruption",
  "Halfling           - You love peace, food, hearth, and home",
  "Lightfoot Halfling - You can easily hide, are inclined to get along with others",
  "Stout Halfling     - Hardier than average and may be part dwarven blood",
  "Human              - It's hard to make generalizations about humans but your human character has these trais\n  Ability Score Increase. Your ability scores each increase by 1.\n  Age. Humans reach adulthood in their late teens and live less than a century.",
  "Dragonborn         - A servant to dragons, a warrior, or a drifter",
  "Gnome              - You delight in life, are an inventor, explorer, and explorer",
  "Forest Gnome       - Knack for illusion and inherent quickness and stealth",
  "Half-Elf           - Curious, inventive, ambitious, love nature, artistic",
  "Half-Orc           - Adventurer with savage fury and barbaric customs",
  "Tiefling           - Demonic heritage, self-reliant, suspicious, drifter"
]

class_desc = [
  "Barbarian          - The relentless combatant fueld by fury.",
  "Bard               - A story witty storyteller or musician.",
  "Cleric             - A holy man capable of helaing wounds.",
  "Druid              - A nomad devoted to the powers of Nature",
  "Fighter            - The skilled combatant and strategist.",
  "Monk               - A martial artist pulling bodily powers.",
  "Paladin            - A novice fighter bolstered by divine magic.",
  "Ranger             - One who blends wilderness knowledge and martial ability",
  "Rogue              - The theif, assassin, and stealthy character.",
  "Sorcerer           - A magic user who draws power from within.",
  "Warlock            - Pacted to a deity for empowering spells.",
  "Wizard             - Keeper of arcane secrets and manipulator of magic."
]

class race_short(Enum):
  HUMAN = "Human"
  ELF = "Elf"
  WOOD_ELF = "Wood Elf"
  HIGH_ELF = "High Elf"
  HALF_ELF = "Half-Elf"
  DWARF = "Dwarf"
  HILL_DWARF = "Hill Dwarf"
  MOUNTAIN_DWARF = "Mountain Dwarf"
  HALFLING = "Halfling"
  LIGHTFOOT_HALFLING = "Lightfoot Halfling"
  STOUT_HALFLING = "Stout Halfling"
  DROW = "Drow"
  DRAGONBORN = "Dragonborn"
  GNOME = "Gnome"
  FOREST_GNOME = "Forest Gnome"
  HALF_ORC = "Half-Orc"
  TIEFLING = "Tiefling"

class class_short(Enum):
  BARBARIAN = "Barbarian"
  BARD = "Bard"
  CLERIC = "Cleric"
  DRUID = "Druid"
  FIGHTER = "Fighter"
  MONK = "Monk"
  PALADIN = "Paladin"
  RANGER = "Ranger"
  ROGUE = "Rogue"
  SORCERER = "Sorcerer"
  WARLOCK = "Warlock"
  WIZARD = "Wizard"


class App(npyscreen.NPSAppManaged):
  def onStart(self):
    self.race = self.addForm(
      'MAIN',
      RacePicker, 
      name = 'Pick your player-character\'s race'
    )
    self.cls = self.addForm(
      'CLASS',
      ClassPicker, 
      name = 'Pick your player-character\'s class'
    )

def main():
  try:
    app = App()
    app.run()
    result =  app, \
              app.race.selection.values[app.race.selection.value[0]], \
              app.cls.selection.values[app.cls.selection.value[0]]
    return result
  except KeyboardInterrupt:
    sys.exit(0)

if __name__ == "__main__":
  result = main()
  print(result)