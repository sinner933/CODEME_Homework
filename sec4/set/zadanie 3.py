#Utwórz 2 krotki. Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki, a oraz nieparzystych elementów z drugiej.

list = []
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

for i in a:
    if i%2 == 0:
        list.append(i)

for i in b:
    if i%2 == 1:
        list.append(i)

print(list)

list.append(a[1::2]+ b[0::2])
print(list)