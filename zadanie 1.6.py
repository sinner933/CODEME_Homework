#Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl komunikat “gratulacje!”, w przeciwnym razie “pudło!”.

counter = int(input("Give me a number "))
a = 1
b = 100
if a <= counter <= b:
    print("gratulacje!")
else:
    print("pudło")
