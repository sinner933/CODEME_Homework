#Utwórz listę, która zawiera składniki na ulubione danie. Wyświetl komunikaty co należy pokolei dodać. Poza pętlą umieść pozostałe instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”.

amount = int(input("Amount of ingridients "))
instructions = input("Other instructions? ")

list = []
for i in range (0, amount):
    list.append(input("give name of " + str(i+1) + " ingridient "))
for i in range(0, amount):
    print(list[i])
print("Other instructions: ",instructions)