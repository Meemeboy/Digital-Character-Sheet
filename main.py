import Character_Sheet as cha
import os, random


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
        choice = int(input("What would you like to add in " + statName))
        if choice > points:
          print("Not enoigh points")
        else:
          break
      points = points - choice
      stats[i] = stats[i] + choice
      if stats[i] >= 15:
        print("Stat cannot be above 15")
        points = points + choice
        stats[i] = stats[i] - choice
        print("You have ",points," points")
        print("You have ",stats[i],"points in ",statName)
        continue
      print("You have ",points," points")
      print("You have ",stats[i],"points in ",statName)



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
  stats = createStats()

  ##return cha.Player(xp,hp,stats,pc,race,statsmod,subclass)


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

test = loadClasses()
characterCreate(test)