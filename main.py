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

def characterCreate(classes):
  print("please choose from the following classes")
  ##display array of loaded classes
  count = 0
  for i in classes:
    count = count + 1 
    print(str(count)+" " + i.name)##prints loaded classes
  choice = int(input(""))
  pc = classes[choice - 1]
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