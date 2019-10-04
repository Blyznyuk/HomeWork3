a = input("Введи строку:")
if len(a) % 2:
   a1 = a[len(a) // 2 + 1:] + a[:len(a) // 2 + 1]
else:
   a1 = a[len(a) // 2:] + a[:len(a) // 2]
print(a1)
