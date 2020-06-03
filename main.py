import Character_Sheet as cha
paladin = cha.loadClass("Paladin/test")
erika = cha.Player(3000,10,[10,10,10,10,10,10],paladin,"test",[0,0,0,0,0,0],None)
subclasses = cha.loadSubclass("Paladin/subclasses")

'''
s = erika.toJSON()
with open("saves","w") as f:
  f.write(s)


'''
erika.levelUp(3,subclasses)
erika.showAbilities()

