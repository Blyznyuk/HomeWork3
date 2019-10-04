#ex5

a = input("Введите значение 1: ")
b = input("Введите значение 2: ")
try:
    c = float(a) + float(b)
    print(c)
except ValueError:
    print(a + b)




