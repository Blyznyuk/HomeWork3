
def my_input():
    while True:
        x = input("Введи число ")
        try:
            x = int(x)
        except ValueError:
            print("Введено не число")
        else:
            return x


a = my_input()
print(a)

def my_word():
    while True:
        x = input("Введи слово ")
        x = x.strip()
        c = x.count(' ')
        if c > 0:
            print("Введено более одного слова")
        else:
            return x


b = my_word()
print(b)


def year():
    while True:
        try:
            a = int(input("Введите год    "))
        except ValueError:
            print("ne chislo")
        else:
            if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
                y = True
            else:
                y = False

            return y


yy = year()
print(yy)



a = int(input("Введите сторону "))
b = int(input("Введите сторону "))
c = int(input("Введите сторону "))


def treygolnick(a, b, c):
    if a <= b+c and b <= a+c and c <= a+b:
        if a == b == c:
            y = "Equilateral triangle"
            return y
        elif a==b or a==c or b==c:
            y = "Isosceles triangle"
            return y
        else:
            y = "Versatile triangle"
            return y
    else:
        y = "Not a triangle"
        return y


y = treygolnick(a,b,c)
print(y)


x = int(input("Введите x "))
y = int(input("Введите y "))
x1 = int(input("Введите x1 "))
y1 = int(input("Введите y1 "))


def rastoyanie(x, y, x1, y1):
    z = ((x - x1)**2 + (y - y1)**2)**0.5
    return z


zz = rastoyanie(x, y, x1, y1)
print(zz)