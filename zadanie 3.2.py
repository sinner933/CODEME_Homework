#Napisz grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 (np. secret_num = 5). Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.

import random

secret_num = random.randrange(0, 20, 1)
a = 0
while a == 0:
    user_num = int(input("Give number  from 0 to 20 "))
    if secret_num == user_num:
        print("That's the right one!")
        a = a + 1
    else:
        print("Wrong")
        continue