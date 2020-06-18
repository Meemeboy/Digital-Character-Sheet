import Character_Sheet as cha
paladin = cha.loadClass("Classes/Paladin/test")
erika = cha.Player(3000,10,[10,10,10,10,10,10],paladin,"test",[0,0,0,0,0,0],None)
subclasses = cha.loadSubclass("Classes/Paladin/subclasses","Paladin")

'''
s = erika.toJSON()
with open("saves","w") as f:
  f.write(s)


'''
erika.levelUp(3,subclasses)
erika.showAbilities()

