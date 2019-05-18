#Utwórz zmienną przechowującą dowolny ciąg znaków. Sprawdź czy string jest dłuższy od 5 oraz czy zawiera literę a. Jeśli zawiera, wszystkie litery a podmień na z.

nadanie = input("Nadaj slowo ")
lenght = len(nadanie) < 5

solution = (print("too short") if lenght else nadanie.replace("a", "z"))
print(solution)