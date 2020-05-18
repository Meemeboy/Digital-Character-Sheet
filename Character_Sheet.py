
class PlayerClass:
  def __init__(self,hitdice,saving,skills,abilities,spells):
    self.hitdice = hitdice
    self.saving = saving
    self.skills = skills
    self.abilities = abilities


class Player:
  def __init__(self,xp,hp,stats):
    self.xp = xp
    self.hp = hp
  def returnLevel(self): ##return total level
    level = 0
    xpamounts = [0,300,900,2700,6500,14000,23000,34000,48000,64000,85000,100000,120000,140000,165000,195000,225000,265000,305000,355000]
    for i in range(20):
      if self.xp < i:
        break
      self.xp = self.xp - xpamounts[i]
      level = level + 1
    return level
    


def loadClass(filename):
  with open(filename) as f:
    hitdice = f.readline()
    savingtemp = f.readline()
    saving = savingtemp.split()
    skillstemp = f.readline()
    skills = skillstemp.split()
    abilities = []
    spells = []
    for i in range(20):
      abilities.append(f.readline().split("£"))
    for i in range(9):
      spells.append(f.readline().split("£"))
  return PlayerClass(hitdice,saving,skills,abilities,spells)

def createClass():
  try:
    hitdice = int(input(""))
  except:
    raise TypeError


    
##ABILITY LAYOUT, 2d Array for each level