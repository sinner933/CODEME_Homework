import random


def mob_hp(hp, lvl):
    if lvl <= 5:
        for i in range(1, 5):
            hp = hp + random.randrange(1, 6)
    elif lvl > 5:
        for i in range(1, 10):
            hp = hp + random.randrange(3, 18)
    return hp


def mob_damage(damage, lvl):
    if lvl <= 5:
        for i in range(1, 2):
            damage = damage + random.randrange(1, 3)
    elif lvl > 5:
        for i in range(1, 4):
            damage = damage + random.randrange(3, 8)
    return damage


angry_mob_damage = mob_damage(0, 1)
angry_mob_health = mob_hp(0, 1)
