#Napisz funkcje, która pyta użytkownika o pary, książka + ocena i zapisuje je w programie.

list1 = []
counter = int(input("How many books? "))
for i in range(counter):
    book = input("Name of the book " + str(i+1) + ": ")
    grade = input("Grade for " + book + ": ")
    list1.append([book, grade])
for i in range(counter):
    print("Name: ", list1[i][0], "Grade ", list1[i][1])