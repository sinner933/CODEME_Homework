#Napisz funkcje, ktora zapyta o numer ksiazki i wyswietli film wraz z ocena

list1 = []
number = int(input("How many files "))

for i in range(number):
    book = input("Name of the " + str(i+1) + " book ")
    film = input("Name of " + book + " grade film ")
    list1.append([book, film])

user_numb = int(input("Give the number of the book "))

if user_numb > number:
    print("Wrong number")
else:
    print(list1[user_numb][1])