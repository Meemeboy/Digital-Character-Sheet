
class PlayerClass:
  def __init__(self,hitdice,saving,skills,abilities,spells):
    self.hitdice = hitdice
    self.saving = saving
    self.skills = skills
    self.abilities = abilities

def loadClass(filename):
  with open(filename) as f:
    hitdice = f.readline()
    savingtemp = f.readline()
    saving = savingtemp.split()
    skillstemp = f.readline()
    skills = savingtemp.split()
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