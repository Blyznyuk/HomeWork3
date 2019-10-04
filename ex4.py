#ex4

a = list(input("Введите список чисел: "))
print(a)
while a:
    print("Удаляемый элемент", a.pop(0))

print("Итоговый масив", a)

a = list(input("Введите список чисел: "))
for i in range(len(a)+1):
    try:
        print("Массив", a[i:])
        print("Удаляемый элемент ", a[i])

    except:
        break


a = int(input("Введите количество чисел: "))
s = []
for i in list(range(a)):
    i = int(input("Введите число "))
    s.append(i)
print("Входной массив ", s)
s.sort()
while s:
   print("Удаляемый элемент", s.pop(0))
print(s)


a = int(input("Введите количество чисел: "))
b = 0
s = []
for i in list(range(a)):
    i = int(input("Введите число "))
    s.append(i)
s.append(0)
print(s)
for i in range(len(s)-1):
    if s[i-1] == s[i]:
        b += 1
    else:
        i += 1
print(b)
























