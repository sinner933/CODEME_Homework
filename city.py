import mobs_module as mobmod
import fight_module as fm


def healing(max_hp):
    hp = max_hp
    return hp


def forest(lvl):
    mob_hp = 0
    mob_damage = 0
    mob_health = mobmod.mob_hp(mob_hp, lvl)
    mob_dmg = mobmod.mob_damage(mob_damage, lvl)
    return mob_health, mob_dmg


def start(hero_hp, hero_damage, maximum, level, experience):
    x = 0
    player_hp = 0
    mob_hp = 0
    decide = int(input('If You want to heal(and see your damage), write 1, if you want to go on a hunt, write 2 '))
    if decide == 1:
        hero_hp = healing(maximum)
        print("You have ", maximum, " hp now. Your damage is ", hero_damage)
    elif decide == 2:
        how_many = int(input('How many enemies you want to kill?'))
        for i in range(0, how_many):
            mob_health, mob_dmg = forest(level)
            print("")
            hero_hp, mob_hp = fm.fight(hero_hp, hero_damage, mob_health, mob_dmg)
            if mob_hp == 0:
                experience = experience + 25
                print('Your experience =', experience)
            elif hero_hp == 0:
                print('You died')
                break
            print("Enemy № ", i+1, 'is dead! You have ', hero_hp, 'hp left')
            if i + 1 == how_many:
                break
            x = int(input("You want to continue hunt? 1 - yes, 2 - no"))
            if x == 2:
                break
        return hero_hp, experience
    else:
        print("Please, try again!")
    return hero_hp, experience

