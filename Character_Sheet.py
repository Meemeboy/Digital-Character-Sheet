import time,json ,os
class PlayerClass:
  def __init__(self,hitdice,saving,skills,abilities,spells,playerchoice,name): ## add subclass
    self.name = name
    self.hitdice = hitdice
    self.saving = saving
    self.skills = skills
    self.abilities = abilities
    self.playerchoice = playerchoice
    self.spells = spells
    mods = [0,0,0,0,0,0]

class Subclass:
  def __init__(self,abilities,spells):
    self.abilities = abilities
    self.spells = spells


class Race:
  def __init__(self,bonus,ability):
    self.ability = ability
    self.bonus = bonus

class Item:
  def __init__(self,description):
    self.description = description

class Player:
  def __init__(self,xp,hp,stats,pc,race,statsmod,subclass,inventory,name):
    self.name = name
    self.xp = xp
    self.hp = hp
    self.pc = pc
    self.stats = stats##str,dex,con,int,wis,cha
    self.statsmod = statsmod
    self.ac = 10
    self.acMod = 0
    self.toHit = 0
    self.toHitMod = 0
    self.inventory = inventory
  def returnLevel(self): ##return total level
    level = 0
    xpamounts = [0, 300, 900, 2700, 6500, 14000, 23000, 34000, 48000, 64000, 85000, 100000, 120000, 140000, 165000,195000, 225000, 265000, 305000, 355000]
    for i in range(20):
      if self.xp < xpamounts[i]:
        break
      level = level + 1
    return level
  def showAbilities(self):##returns array containing all abilities
    output = []
    for i in range(self.returnLevel()):
      output.append(self.pc.abilities[i])
    output.append(self.pc.abilities[20])
    return output
  def levelStat(self):
    print("1-Strength \n2-Dexterity \n3-Constitution \n4-Intelligence \n5-Wisdom \n6-Charisma")
    choice1 = int(input("What stat would you like to increase?(1-6)"))
    choice2 = int(input("What stat would you like to increase?"))
    self.stats[choice1 - 1]= self.stats[choice1 - 1] + 1
    self.stats[choice2 - 1]= self.stats[choice2 - 1] + 1
  def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
  def levelUp(self,level,subclasses):
    xpamounts = [0, 300, 900, 2700, 6500, 14000, 23000, 34000, 48000, 64000, 85000, 100000, 120000, 140000, 165000,195000, 225000, 265000, 305000, 355000]
    self.xp = xpamounts[level - 1]
    if level == 3:
      yeet = os.listdir("Classes/"+self.pc.name+"/subclasses")## replace with correct class
      print(yeet)
      choice = int(input("Please select which subclass from the above choice"))
      self.subclass = subclasses[choice-1]
      self.pc.abilities[2].append(self.subclass.abilities[0])
    print(self.pc.abilities[level-1])
    for i in self.pc.playerchoice[level-1]:
        print(i)
        print("\n")
    if self.pc.playerchoice[level-1][0] == "CHS1":
      choices = 1
    else:
      choices = 0
    for i in range(choices):
      choice = int(input("Please select an option from the above choices(num)"))
      if self.pc.playerchoice[level-1][choice][0] == "A":
        mod = int(self.pc.playerchoice[level-1][choice][2])
        self.acMod = self.acMod + mod
      if self.pc.playerchoice[level-1][choice][0] == "H":
        mod = int(self.pc.playerchoice[level-1][choice][2]) ##Finds modifier from string
        self.toHitMod = self.toHitMod + mod
      if self.pc.playerchoice[level-1][choice][0] == "Z":
        self.pc.abilities[20].append(self.pc.playerchoice[level-1][choice])
  def returnSpells(self,spellslist):
    highest = 0
    spells = []
    outspells = []
    count = 0
    level = self.returnLevel()
    secondarySpell = [2,5,9,13,17]
    for i in secondarySpell:
      if level < i:
        break
      highest = secondarySpell.index(i)
    for j in range(highest + 2):
      spells.append(self.pc.spells[j])
    for i in spells:
      for j in i:
        j = j[:-1]
        j = j.replace("_"," ")
        outspells.append(j)
    '''
    for i in outspells:
      for j in spellslist:
        if i == j.name:
          print("replacing ", i, " with ", j.name)
          outspells[count] = j
          continue
      count += 1
    '''
    for i in outspells:
      outspells[count] = spellslist.get(i,None)
      print(outspells[count])
      count += 1
    ##find the object for each spell and add it to array instead of string
    return outspells

class Spell:
  def __init__(self,name,casttime,components,ability,duration,level,srange,school):
    self.name = name
    self.casttime = casttime
    self.range = srange
    self.school = school
    self.components= components
    self.duration = duration
    self.level = level
    self.ability = ability

def loadSpells():
  spelllist = {}
  with open("spells.json", encoding = "utf-8") as f:
    yeet = json.loads(f.read())
    f.close()
  for x,y in yeet.items():
    spellyeet = []
    spellyeet.append(x)
    for j,l in y.items():
      spellyeet.append(l)
    spelllist[spellyeet[0]] = Spell(spellyeet[0],spellyeet[1],spellyeet[2],spellyeet[3],spellyeet[4],spellyeet[5],spellyeet[6],spellyeet[7]) ##Initialises spells and creates key pairs
  return spelllist


def loadSubclass(directory,classname):
  subclasses = []
  for i in os.listdir(directory):
    print("Loading",i)
    with open("Classes/"+classname+ "/subclasses/"+i,"r", encoding = "utf-8") as f: ## replace paladin with class
      subabilities = []
      spells = []
      for i in range(5):
        subabilities.append(f.readline().split("£"))
      for i in range(9):
        spells.append(f.readline().split("£"))
      subclasses.append(Subclass(subabilities,spells))
  print("\n")
  return subclasses


def loadClass(filename):
  with open(filename) as f:
    hitdice = f.readline()
    savingtemp = f.readline()
    saving = savingtemp.split()
    skillstemp = f.readline()
    skills = skillstemp.split()
    abilities = []
    spells = []
    playeractions = []
    for i in range(20):
      abilities.append(f.readline().split("£"))
      playeractions.append(f.readline().split("£"))
    for i in range(10):
      spells.append(f.readline().split("£"))
    abilities.append([])
    name = f.readline()
  return PlayerClass(hitdice,saving,skills,abilities,spells,playeractions,name)

def createClass():
  try:
    hitdice = int(input("input the class' hitdice(e.g.6"))
  except:
    raise TypeError





##ABILITY LAYOUT, 2d Array for each level