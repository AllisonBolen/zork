from random import *
from Observable import *
from NPCS.NPC import *

class Vampire(NPC):

    ''' Vampires attack at a rate of 10-20 HP per turn. They are not harmed by
    ChocolateBars. Start with 100-200 HP. '''

    def __init__(self):
        NPC.__init__(self)
        self.attack = randint(10, 20)
        self.hp = randint(100, 200)
        self.candy = ['ChocolateBars']  # candy its not hurt by
        self.special = []

    # helper funcs
    def genAttack(self):
        self.attack = randint(10, 20)
        return self.attack
