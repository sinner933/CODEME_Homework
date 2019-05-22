#Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi na funkcję obliczającą bmi na podstawie danych użytkownika oraz zwracającą odpowiednią wartość (niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru.

a = 0

def bmi(a):
    weight = float(input("Weight "))
    height = float(input("Height in meters "))
    bmi = weight/(height**2)
    a = bmi
    return a
z = bmi(a)
print(z)
if z < 19:
    print("Low weight")
if 19 <= z < 25:
    print("Normal")
if 25 <= z < 30:
    print("Overweight")
if 30 <= z < 40:
    print("Obese")