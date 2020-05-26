
class PlayerClass:
  def __init__(self,hitdice,saving,skills,abilities,spells,playerchoice): ## add subclass
    self.hitdice = hitdice
    self.saving = saving
    self.skills = skills
    self.abilities = abilities
    self.playerchoice = playerchoice
    mods = [0,0,0,0,0,0]

class Subclass:
  def __init__(self):
    return True


class Race:
  def __init__(self,bonus,ability):
    self.ability = ability

class Player:
  def __init__(self,xp,hp,stats,pc,race,statsmod):
    self.xp = xp
    self.hp = hp
    self.pc = pc
    self.stats = stats##str,dex,con,int,wis,cha
    self.statsmod = statsmod
    self.ac = 10
    self.acMod = 0
    self.toHit = 0
    self.toHitMod = 0
  def returnLevel(self): ##return total level
    level = 0
    xpamounts = [0,300,900,2700,6500,14000,23000,34000,48000,64000,85000,100000,120000,140000,165000,195000,225000,265000,305000,355000]
    for i in range(20):
      if self.xp < xpamounts[i]:
        break
      level = level + 1
    return level
  def showAbilities(self):
    print("\n")
    for i in range(self.returnLevel()):
      for x in range(len(self.pc.abilities[i])):
        print(self.pc.abilities[i][x])
        print("\n")
    print(self.pc.abilities[20])
  def levelStat(self):
    print("1-Strength \n2-Dexterity \n3-Constitution \n4-Intelligence \n5-Wisdom \n6-Charisma")
    choice1 = int(input("What stat would you like to increase?(1-6)"))
    choice2 = int(input("What stat would you like to increase?"))
    self.stats[choice1 - 1]= self.stats[choice1 - 1] + 1
    self.stats[choice2 - 1]= self.stats[choice2 - 1] + 1

  def levelUp(self,level):
    print(self.pc.abilities[level-1])
    for i in self.pc.playerchoice[level-1]:
        print(i)
        print("\n")
    if self.pc.playerchoice[level-1][0] == "CHS1":
      choices = 1
    for i in range(choices):
      choice = int(input("Please select an option from the above choices"))
      if self.pc.playerchoice[level-1][choice][0] == "A":
        mod = int(self.pc.playerchoice[level-1][choice][2])
        self.acMod = self.acMod + mod
      if self.pc.playerchoice[level-1][choice][0] == "H":
        mod = int(self.pc.playerchoice[level-1][choice][2]) ##Finds modifier from string
        self.toHitMod = self.toHitMod + mod
      if self.pc.playerchoice[level-1][choice][0] == "Z":
        self.pc.abilities[20].append(self.pc.playerchoice[level-1][choice])





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
    for i in range(9):
      spells.append(f.readline().split("£"))
    abilities.append([])
  return PlayerClass(hitdice,saving,skills,abilities,spells,playeractions)

def createClass():
  try:
    hitdice = int(input(""))
  except:
    raise TypeError


    
##ABILITY LAYOUT, 2d Array for each level