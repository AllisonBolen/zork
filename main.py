import Game


def main():
    game = Game.Game()
    game.run()
    # #weapons
    # cb = ChocolateBars.ChocolateBars()
    # nb = NerdBomb.NerdBomb()
    # hk = HersheyKisses.HersheyKisses()
    # ss = SourStraws.SourStraws()
    #
    # # mess with weapons
    # print(cb.getUses())
    # print(nb.getUses())
    # print(hk.getUses())
    # print(ss.getUses())
    #
    # # monsters
    # gh = Ghouls.Ghouls()
    # pr = Person.Person()
    # vp = Vampire.Vampire()
    # ww = Werewolves.Werewolves()
    # zb = Zombie.Zombie()
    #
    # # mess with monsters
    # monstList = [gh,pr,vp,ww,zb]
    # for mst in monstList:
    #     hp = mst.getHP()
    #     print('Health: {}'.format(hp))
    #     at = mst.genAttack()
    #     print('attack gend: {}'.format(at))
    # # home
    # hm = Home.Home()
    # p = Player.Player()
    #
    # for w in p.getInventory():
    #     n = w.getName()
    #     m = w.genModif()
    #     print('weapon: {name}, modifier: {modif}'.format(name=n, modif=m))
    #
    # n = Neighborhood.Neighborhood(4)
    #
    # numM = n.getCount() # neighborhodd total
    # print('Num monsters: {}'.format(numM))
    #
    # print(n.getGrid()[1][1].getMonsters())
    # hmnumM = n.getGrid()[1][1].getNumMonsters()
    # print('before kill: {}'.format(hmnumM))
    # n.getGrid()[1][1].killMonster(1)
    #
    # hmnumM = n.getGrid()[1][1].getNumMonsters()
    # print('after Kill kill: {}'.format(hmnumM))
    #
    # print(n.getGrid()[1][1].getMonsters())
    #
    # numM = n.getCount() # neighborhodd total
    # print('Num monsters: {}'.format(numM))



if __name__ == "__main__":
    main()
