import Character_Sheet as cha
paladin = cha.loadClass("test")
erika = cha.Player(1000,10,[10,10,10,10,10,10],paladin,"test",[0,0,0,0,0,0])
s = erika.toJSON()
with open("saves","w") as f:
  f.write(s)
'''
print(erika.returnLevel())
erika.levelUp(2)
erika.levelStat()
erika.showAbilities()
'''




