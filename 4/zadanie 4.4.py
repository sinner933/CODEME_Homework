#Napisz grę - kamień (k) / papier (p) / nożyce (n).
import random
a = 0
b = 1
user_inp = input("nadaj kamień - k / papier - p / nożyce - n ")
comp_inp = random.randrange(1, 3, 1)

if user_inp == "k":
    user_inp = 1
elif user_inp == "p":
    user_inp = 2
elif user_inp == "n":
    user_inp = 3
else:
    print("nieprawidlowo nadane dane")

if user_inp == comp_inp:
    print("Remis")


while user_inp == 1:
    if comp_inp == 3:
        print("wictoria")
    elif comp_inp == 2:
        print("porażka")
    break
while user_inp == 2:
    if comp_inp == 1:
        print("wictoria")
    elif comp_inp == 3:
        print("porażka")
    break
while user_inp == 3:
    if comp_inp == 2:
        print("wictoria")
    elif comp_inp == 1:
        print("porażka")
    break