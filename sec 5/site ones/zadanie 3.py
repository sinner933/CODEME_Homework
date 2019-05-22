#Napisać funkcję, która przyjmuje listę liczb i zwraca sumę wszystki elementów na liście.

list_of_numbers = []
number = int(input("How many numbers? "))
suma = 0
answer = []

for i in range(number):
    user_input = int(input("Give number "))
    list_of_numbers.append(user_input)

for i in range(number):
    suma = suma + list_of_numbers[i]

print(suma)