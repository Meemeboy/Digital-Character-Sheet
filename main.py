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

class MyGrid(GridLayout):
    ##self.display.text = self.outArray[self.posIndex]
    pass



class CharacterSheet(App):
  def build(self):
    return MyGrid()




def loadClasses():
  classArray = []
  for filename in os.listdir("Classes"):
    try:
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
        choice = int(input("What would you like to add in " + statName))
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
  choice = int(input("Please input which character to load(1-" + str(len(dirlist)) + ")"))
  choicef = dirlist[choice-1]
  with open("Saves/" + choicef,"rb") as f:
    loadedCha = pickle.load(f)
  return loadedCha

    
    


'''
paladin = cha.loadClass("Classes/Paladin/test")
erika = cha.Player(3000,10,[10,10,10,10,10,10],paladin,"test",[0,0,0,0,0,0],None)
subclasses = cha.loadSubclass("Classes/Paladin/subclasses","Paladin")


s = erika.toJSON()
with open("saves","w") as f:
  f.write(s)



erika.levelUp(3,subclasses)
erika.showAbilities()


test = cha.loadSpells()
print(len(test))
print(test[125].ability)
'''

subclasses = cha.loadSubclass("Classes/Paladin/subclasses","Paladin")
spellsCache = cha.loadSpells() ##caches the loaded spells
classCache = loadClasses()
##testC = characterCreate(classCache)
##saveCharacter(testC)
CharacterInstance = loadCharacter()
CharacterInstance.levelUp(2, subclasses)
saveCharacter(CharacterInstance)
print("Character level is " , CharacterInstance.returnLevel())
print("All spells at this level are " , CharacterInstance.returnSpells(spellsCache))

##if __name__ == "__main__":
  ##CharacterSheet().run()