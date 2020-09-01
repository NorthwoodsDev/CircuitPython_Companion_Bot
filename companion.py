import random

class companbot:
    def __init__(self, lvl, xp, cred, hunger, hp, pAtk, pDef):
        self.lvl = lvl
        self.xp = xp
        self.cred = cred
        self.hunger = hunger
        self.hp = hp
        self.pAtk = pAtk
        self.pDef = pDef
        return

    def levelUp(companbot_x):
        try:
            companbot_x.hp = int(companbot_x.hp) + random.randint(1,5)
            companbot_x.pAtk = int(companbot_x.pAtk) + random.randint(1,3)
            companbot_x.pDef = int(companbot_x.pDef) + random.randint(1,5)
            companbot_x.lvl = int(companbot_x.lvl) + 1
            companbot_x.xp = companbot_x.xp - 100
        except Exception as e:
            print("Error Level Up: " + str(e))
        return companbot_x