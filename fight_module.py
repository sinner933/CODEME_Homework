def hero_damages(mob_hp, hero_damage):
    mob_hp_temporary = mob_hp - hero_damage
    if mob_hp_temporary < 0:
        print("Enemy dies! Congratulations!")
        mob_hp_temporary = 0
    return mob_hp_temporary


def mob_damages(hero_hp, mob_damage):
    hero_hp_temporary = hero_hp - mob_damage
    if hero_hp_temporary < 0:
        print("You are dead")
        hero_hp_temporary = 0
    return hero_hp_temporary


def fight(hero_hp, hero_damage, mob_hp, mob_damage):
    while hero_hp != 0 or mob_hp != 0:
        mob_hp_temporary = hero_damages(mob_hp, hero_damage)
        hero_hp_temporary = mob_damages(hero_hp, mob_damage)
        hero_hp = hero_hp_temporary
        mob_hp = mob_hp_temporary
        print("Mob hp = ", mob_hp, "Hero hp = ",  hero_hp)
        if hero_hp == 0:
            break
        elif mob_hp == 0:
            break
        decision = int(input("You want to stop fight? 1 - no, 2 - yes"))
        if decision == 2:
            break
    return hero_hp, mob_hp
