# a = list(input("Введите список чисел: "))
# print(a)
# while a:
#     print("Удаляемый элемент", a.pop(0))
#
# print("Итоговый масив", a)
#
# a = list(input("Введите список чисел: "))
# for i in range(len(a)+1):
#     try:
#         print("Массив", a[i:])
#         print("Удаляемый элемент ", a[i])
#
#     except:
#         break

while True:
    a = list(input("Введите список чисел: "))
    try:
        for i in range(len(a)):
            a[i] = a[i]/1
        print(a)
    except:
        print("ch")














