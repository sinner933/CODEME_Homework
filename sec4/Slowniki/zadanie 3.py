#Utwórz dowolną tablicę n x n zawierającą dowolny znak, a następnie wyświetl jej elementy w formie tabeli n x n. Elementy powinny być oddzielone spacją

rozmiar = int(input("how big?"))
a = [['-'] * rozmiar] * rozmiar

for row in a:
    print(" ".join(row))

