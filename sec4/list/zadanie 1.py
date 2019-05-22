#Stwórz listę przedmiotów, które zabierzesz na samotną wyprawę w góry. Elementy na liście posortuj alfabetycznie, a następnie wyświetl.

Items = []
for i in range(0, 5):
    item = input("give item, to the island")
    Items.append(item)

Items.sort()
print(Items)
