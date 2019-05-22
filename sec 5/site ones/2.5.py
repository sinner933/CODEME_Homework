import random

def differnce(a, b):
    diff = a - b
    return diff

def hola(num):
    if num < 0:
        return (-num)

def hot(a, b):
    if a < b:
        print("Hot")

def cold(a, b):
    if a < b:
        print("cold")

user_input1 = int(input("Give the number"))

secret_num = random.randrange(1, 100)

secret = differnce(secret_num, user_input1)

while user_input1 != secret_num:
    print(secret_num)
    print("Wrong ")
    new_one = int(input("Give new number "))
    if new_one == secret_num:
        print("Right one ")
    else:
        z = differnce(secret_num, new_one)
        z = hola(z)
        hot(int(z), secret)
        cold(secret, int(z))
    user_input1 = new_one