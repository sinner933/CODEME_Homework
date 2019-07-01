import random
import fight_module as fm


def initiative(bonus, target):
    target = random.randrange(1, 20) + bonus
    return target


def hero_start(mob_armor, hero_attack, mob_hp, hero_damage, hero_armor, mob_attack, hero_hp, mob_damage, hero_result, mob_result):
    hero_result = fm.hero_strike(mob_armor, hero_attack, mob_hp, hero_damage)
    mob_result = fm.mob_strike(hero_armor, mob_attack, hero_hp, mob_damage)
    return hero_result, mob_result


def mob_start(mob_armor, hero_attack, mob_hp, hero_damage, hero_armor, mob_attack, hero_hp, mob_damage, hero_result, mob_result):
    mob_result = fm.mob_strike(hero_armor, mob_attack, hero_hp, mob_damage)
    hero_result = fm.hero_strike(mob_armor, hero_attack, mob_hp, hero_damage)
    return hero_result, mob_result


def battle_result(flee, lose, win):
    if flee == 1:
        print("You ran away")
    elif lose == 1:
        print("You died, restart?")
    elif win == 1:
        exp = hero_exprience(Hero_exp, mob_lvl)
        return exp
