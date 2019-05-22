#Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.

counts = []

for i in range(0, 5):
    cyfra = input("nadaj cyfre")
    counts.append(cyfra)

if counts[0] == counts[-1]:
    print("first and last are same")
else:
    print("first and last are different")
