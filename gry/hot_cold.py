import random

def difference(num):
    if num < 0:
        num = -num

secret_number = random.randrange(0, 100)

differ = 0
previous = 0

user_number = int(input("Give your number from 0 to 100"))

while user_number != secret_number:
    differ = user_number - secret_number
    user_number = int(input("Wrong, give new one"))
    if differ > previous:
