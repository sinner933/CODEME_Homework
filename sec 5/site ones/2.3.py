#Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).

#def maximum_of(a,b,c):
#    if a < b:
#        if c < b:
#            print(b + "is maximum")
#    if b < c:
#        if a < c:
#            print(c + "is maximum")
#    if b < a:
#        if c < a:
#            print(a + "is maximum")

def max_of_2(x,y):
    if x > y:
        return x
    else:
        return y

def max_of_3(a,b,c):
    # tmp = max_of_2(a, b)
    # return max_of_2(tmp, c)
    return max_of_2(max_of_2(a, b), c)


user_inp1 = int(input("First number "))
user_inp2 = int(input("Second number "))
user_inp3 = int(input("Last number "))

print(max_of_3(user_inp1, user_inp2, user_inp3))