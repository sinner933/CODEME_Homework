import city as ct


class Player:
    def __init__(self, name, experience, health, damage, level, maximum):
        self.name = name
        self.experience = experience
        self.health = health
        self.damage = damage
        self.level = level
        self.maximum = maximum
        print('Class ', name, ': hp=', health, ' , exp=', experience, ' , damage = ', damage, 'level = ', level)


class Knight(Player):
    def __init__(self):
        super().__init__('Knight', 0, 60, 5, 1, 60)


class Archer(Player):
    def __init__(self):
        super().__init__('Archer', 0, 40, 10, 1, 40)


def creation():
    p = int(input('If you want to play Knight - write 1, Archer - 2 '))
    if p == 1:
        player = Knight()
    else:
        player = Archer()
    return player


def lvlup(experience, lvl, maximum, damage):
    requier = lvl * 100
    if experience >= requier:
        print("Congratulations! You get a level!You receive +10 hp and +5 dmg")
        maximum += 10
        damage += 5
        experience -= requier
        lvl = lvl + 1
    return experience, lvl, maximum, damage


x = 0
player = creation()
while x != 2:
    x = int(input("If you want to continue write 1, if you want to stop, write 2 "))
    if x == 2:
        break
    player.health, player.experience = ct.start(player.health, player.damage, player.maximum, player.level, player.experience)
    if player.health == 0:
        break
    player.experience, player.level, player.maximum, player.damage = lvlup(player.experience, player.level, player.maximum, player.damage)

print('Thank you for participation')