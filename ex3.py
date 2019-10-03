a = 0
while a < 11:
    print(a)
    a += 1


b = 20
while b > 0:
    print(b, end=' ')
    b -= 1



s = []
c = 20
print(sep='\n')
while c > 0:
    s.append(c)
    c -= 1
print(s)


while True:
    d = int(input("Введите четное число: "))
    if d%2 !=0 :
        print("Введено нечетное число. Повторите ввод")
    else:
        e = 0
        while d//2:
            e += 1
            if (d//2) % 2 == 0:
                d = d//2
            else:
                break
        print(e)
        break
