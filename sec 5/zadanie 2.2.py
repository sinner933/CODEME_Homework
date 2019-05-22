def uzuoelnij_biblioteke():
    biblioteka = {}
    ile = int(input("How many books? "))
    for i in range(ile):
        tytul = input("Give the name of the book: ")
        ocena = input("Give the grade")
        biblioteka[tytul] = ocena
    return biblioteka

def znajdz_ksiazke(tytul):
    print("Grade of chosen book", tytul, "to", biblioteka[tytul])