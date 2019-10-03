# a = list(input("Введите строку: "))
# print(a)
# while a:
#     print("Удаляемый элемент", a.pop(0))
#
# print("Итоговая строка", a)
#
# a = list(input("Введите строку: "))
# for i in range(len(a)+1):
#     try:
#         print("Строка", a[i:])
#         print("Удаляемый элемент ", a[i])
#
#     except:
#         break




# a = int(input("Введите количество чисел: "))
# s = []
# for i in list(range(a)):
#     i = int(input("Введите число "))
#     s.append(i)
# print("Входной массив ", s)
# s.sort()
# while s:
#    print("Удаляемый элемент", s.pop(0))
# print(s)

# a = int(input("Введите количество чисел: "))
# b = 0
# s = []
# for i in list(range(a)):
#     i = int(input("Введите число "))
#     s.append(i)
#
# s.append(0)
# print(s)
#
# for i in range(len(s)-1):
#     if s[i-1] == s[i]:
#         b += 1
#     else:
#         i += 1
# print(b)
#
#
prev = -1
curr_rep_len = 0
max_rep_len = 0
element = int(input())
while element != 0:
    if prev == element:
        curr_rep_len += 1
    else:
        prev = element
        max_rep_len = max(max_rep_len, curr_rep_len)
        curr_rep_len = 1
    element = int(input())
max_rep_len = max(max_rep_len, curr_rep_len)
print(max_rep_len)




















