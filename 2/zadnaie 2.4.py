#Napisz program, który wyświetli kolejne wyniki dla silnii liczby naturalnej n.

n = int(input("Give number "))

factorial = 1
list = []

for i in range(2, n + 1):
    factorial *= i

for i in range(0, n):
    list.append(i+1)

print(n, "!=", list.copy(), factorial)