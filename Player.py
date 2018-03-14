from random import *
from NPCS import *
from Weapons import *

class Player(object):
    '''This is you. You have a certain amount of HP, randomly generated
    between 100 - 125. You also have an attack value, between 10-20.
    You are able to hold 10 weapons; these are randomly generated and added
    to your inventory when you are created.'''

    def __init__(self):
        self.inventory = self.populateWeapons()
        self.hp = randint(100, 125)
        self.attack = randint(10, 20)

    def populateWeapons(self):
        hk = HersheyKisses.HersheyKisses() # always have hks
        weaps = [hk]
        for w in range(0, 9):
            popList = ['ChocolateBars', 'NerdBomb', 'SourStraws']
            selected = randint(0, 2)
            if popList[selected] == 'ChocolateBars':
                cb = ChocolateBars.ChocolateBars()
                weaps.append(cb)
            elif popList[selected] == 'NerdBomb':
                nb = NerdBomb.NerdBomb()
                weaps.append(nb)
            elif popList[selected] == 'SourStraws':
                ss = SourStraws.SourStraws()
                weaps.append(ss)
        return weaps

    def genAttack(self):
        self.attack = randint(10,20)
        return self.attack

    # getters
    def getAttack(self):
        return self.attack

    def getHP(self):
        return self.hp

    # setters
    def setAttack(self, a):
        self.attack = a

    def setHP(self, hp):
        self.hp = hp

    def getInventory(self):
        return self.inventory