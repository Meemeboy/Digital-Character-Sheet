import Character_Sheet as cha
import os, random,pickle
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.uix.slider import Slider
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang.builder import Builder
from kivy.graphics.svg import Svg

global sm
global CharacterInstance
global classCache
global stats

class MyGrid(Screen):
    ##self.display.text = self.outArray[self.posIndex]
    slidersp = ObjectProperty(None)
    sliderab = ObjectProperty(None)
    namedisplay = ObjectProperty(None)
    xpdisplay = ObjectProperty(None)
    hpdisplay = ObjectProperty(None)
    sliderle = ObjectProperty(None)

    def on_pre_enter(self, *args):
      self.namedisplay.text = CharacterInstance.name
      self.xpdisplay.text = str(CharacterInstance.xp)
      self.hpdisplay.text = str(CharacterInstance.hp)

    def showSpells(self):
      print(self.slidersp.value)
      text = ""
      spellArray = CharacterInstance.returnSpells(spellsCache)
      for i in spellArray:
        try:
          print("Spell level is ", i.level)
          print("Slider value is ", int(self.slidersp.value))
          if i.level == int(self.slidersp.value):
            text = text + i.name
            text = text + ": "
            text = text + i.ability
            text = text + i.level
            text = text + "\n"
        except:
          pass
      self.display.text = text
    def showAbilities(self):
      self.namedisplay.text = CharacterInstance.name
      self.xpdisplay.text = str(CharacterInstance.xp)
      self.hpdisplay.text = str(CharacterInstance.hp)## Updates top info
      text = ""
      abilityArray = CharacterInstance.showAbilities() ##fetches abilities from class
      print(abilityArray)
      if int(self.sliderab.value) == 0:## outputs inate abilities of character
        for i in abilityArray[0]:
          text = text + i
          text = text + "\n" * 2
        print("Outputting 0th level abilities")
        return None ## exits function
      try:
        for i in abilityArray[int(self.sliderab.value)]: ## adds each level's abilities
          text = text + i
          text = text + "\n" * 2
      except:
        pass
      try:
        for i in abilityArray[int(self.sliderab.value-2)]:
          text = text + i
          text = text + "\n" * 2
      except:
        pass
      try:
        for i in abilityArray[int(self.sliderab.value -3)]:
          text = text + i
          text = text + "\n" * 2
      except:
        pass
      try:
        for i in abilityArray[int(self.sliderab.value-4)]:
          text = text + i
          text = text + "\n" * 2

      except:
        pass
      self.display.text = text
    def levelUp(self):
      if int(self.sliderle.value) != 0:
        CharacterInstance.levelUp(int(self.sliderle.value),subclasses)
        saveCharacter(CharacterInstance)

class MenuScreen(Screen):
  def on_pre_enter(self, *args):
    Characters = loadCharacter()
    ##add input methods
    text = ""
    count = 0

    for i in Characters:
      count += 1
      text = text + str(count)
      text = text + " - "
      text = text + str(i)
      text = text + "\n"
      self.display.text = text
    texte = self.ids.input.text

  def showCharacters(self):
    Characters = loadCharacter()
    ##add input methods
    text = ""
    count = 0

    for i in Characters:
      count += 1
      text = text + str(count)
      text = text + " - "
      text = text + str(i)
      text = text + "\n"
      self.display.text = text
    texte = self.ids.input.text
    print(texte)
    textei = None
    chartemp = None
    try:
      textei = int(texte)
      print("Textei is ", textei)
      chartemp = Characters[textei - 1]
    except:
      pass
    if chartemp != None:
      with open("Saves/" + chartemp,"rb") as f:
        global CharacterInstance
        CharacterInstance = pickle.load(f)
        print("Loaded", CharacterInstance)
        sm.current = 'sheet'

class CreationScreen(Screen):
  def assignStats(self):
    global stats
    stats = [8,8,8,8,8,8]
    strengthval = int(self.ids.strengthin.value)
    dexval = int(self.ids.dexterityin.value)
    conval = int(self.ids.constitutionin.value)
    intval = int(self.ids.intelligencein.value)
    wisval = int(self.ids.wisdomin.value)
    charval = int(self.ids.charismain.value)
    if strengthval + dexval + conval + intval + wisval + charval <= 27 and strengthval < 8 and dexval < 8 and conval < 8 and wisval < 8 and intval < 8 and charval < 8:
      stats[0] += strengthval
      stats[1] += dexval
      stats[2] += conval
      stats[3] += intval
      stats[4] +=wisval
      stats[5] += charval
      print("SUCCESS")
      sm.current = 'personal'  ##next screen
      return stats
    return None


class PersonalScreen(Screen):
  entry = ObjectProperty(None)
  state = False

  def on_pre_enter(self, *args):
    self.selectClass()
  def selectClass(self):
    text = ""
    count = 0
    for i in classCache:
      count += 1
      text = text + str(count) + " " + i.name
    self.entry.text = text
    if self.state == False:
      self.state = True
      return None
    try:
      classChoice = classCache[int(self.ids.classin.text) - 1]
    except:
      return None
    name = self.ids.namein.text
    if name == "":
      return None
    CharacterInstance = cha.Player(0,0,stats,classChoice,"Replace",[0,0,0,0,0,0],None,[],name)
    print(CharacterInstance.name, "Is Complete")
    saveCharacter(CharacterInstance)
    sm.current = 'menu'




class CharacterSheet(App):

  def build(self):
    global sm
    sm = ScreenManager()
    sm.add_widget(MenuScreen(name='menu'))
    sm.add_widget(CreationScreen(name='create'))
    sm.add_widget(PersonalScreen(name='personal'))
    sm.add_widget(MyGrid(name='sheet'))
    sm.current = 'menu'
    return sm




def loadClasses():
  classArray = []
  for filename in os.listdir("Classes"):
    try:
      print("Classes/" + filename + "/main")
      classArray.append(cha.loadClass("Classes/" + filename + "/main"))
    except:
      raise OSError(filename)
  return classArray

def createStats():
  stats = [8,8,8,8,8,8]
  points = 27
  print("Please allocate points for your main 6 abilities")
  while points > 0:
    for i in range(len(stats)):
      if i == 0:
        statName = "Strength"
      if i == 1:
        statName = "Dexterity"
      if i == 2:
        statName = "Constitution"
      if i == 3:
        statName = "Intelligence"
      if i == 4:
        statName = "Wisdom"
      if i == 5:
        statName = "Charisma"
      while True:
        print("You have",stats[i],"points in ",statName)

        if choice > points:
          print("Not enoigh points")
        else:
          break
      points = points - choice
      stats[i] = stats[i] + choice
      if stats[i] > 15:
        print("Stat cannot be above 15")
        points = points + choice
        stats[i] = stats[i] - choice
        print("You have ",points," points")
        print("You have ",stats[i],"points in ",statName)
        continue
      print("You have ",points," points")
      print("You have ",stats[i],"points in ",statName)
      if points == 0:
        break
  return stats



def characterCreate(classes):
  xp = 0
  print("please choose from the following classes")
  ##display array of loaded classes
  count = 0
  for i in classes:
    count = count + 1 
    print(str(count)+" " + i.name)##prints loaded classes
  choice = int(input(""))
  pc = classes[choice - 1]
  hp = pc.hitdice
  while True:
    stats = createStats()
    choice1 = input("Are you happy with these stats?(Y/N)")
    for i in stats:
      print(i)
    if choice1 == "Y":
      break
  name = input("What is your characters name?")
  return cha.Player(xp,hp,stats,pc,"Replace",[0,0,0,0,0,0],None,[],name)

def saveCharacter(obj):
  with open("Saves/" + obj.name,"wb") as f:
    pickle.dump(obj,f)

def loadCharacter():
  count = 0
  dirlist = []
  for filename in os.listdir("Saves"):
    count = count + 1
    print(str(count) +"-"+ filename)
    dirlist.append(filename)
  return dirlist


subclasses = cha.loadSubclass("Classes/Paladin/subclasses","Paladin")
spellsCache = cha.loadSpells() ##caches the loaded spells
classCache = loadClasses()
CharacterInstance = None
if __name__ == "__main__":
  mainApp = CharacterSheet()
  mainApp.run()
