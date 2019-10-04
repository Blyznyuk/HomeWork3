while True:
    a = input("Введи строку:")
    try:
        print(a[2], a[-2], a[:5], a[:-2], a[::2], a[1::2], a[::-1], a[-1::-2], a[-2::-2], a[len(a) - 2:0:-1], len(a), sep='\n')
    except IndexError:
        print("Больше 3х символов")
    else:
        break
