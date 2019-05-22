#Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób, natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód, np:

number = int(input("how many workers? "))
list_of_workesr = []
for i in range(number):
    name = input("Name ")
    surname = input("Surname ")
    job = input("Job ")
    list_of_workesr.append([name, surname, job])

for i in range(number):
    print("Imie: ", list_of_workesr[i][0], " Surname: ", list_of_workesr[i][1], " Job: ", list_of_workesr[i][2])



