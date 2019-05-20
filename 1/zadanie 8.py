#Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych. Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.

first = int(input("give 1 number "))
second = int(input("give 2 number "))
third = int(input("give 3 number "))
list = [first, second, third]
print(sorted(list))
