class Player:
    def __init__(self, name, experience, health, damage, level, maximum):
        print('Class ', name, ': hp=', health, ' , exp=', experience, ' , damage = ', damage, 'level = ', level, 'Max hp = ', maximum)


class Knight(Player):
    def __init__(self):
        super().__init__('Knight', 0, 60, 5, 1, 60)


class Archer(Player):
    def __init__(self):
        super().__init__('Archer', 0, 40, 10, 1, 40)
