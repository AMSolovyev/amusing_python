a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if a == b == c:
    print(a, b, c, sep='\n')
elif a == b:
    if a > c:
        print(a, c, b, sep='\n')
    else:
        print(c, a, b, sep='\n')
elif a == c:
    if a > b:
        print(a, b, c, sep='\n')
    else:
        print(b, a, c, sep='\n')
elif b == c:
    if a > b:
        print(a, b, c, sep='\n')
    else:
        print(b, a, c, sep='\n')
elif a > b and a > c:
    if b > c:
        print(a, c, b, sep='\n')
    else:
        print(a, b, c, sep='\n')
elif b > a and b > c:
    if a > c:
        print(b, c, a, sep='\n')
    else:
        print(b, a, c, sep='\n')
elif c > a and c > b:
    if a > b:
        print(c, b, a, sep='\n')
    else:
        print(c, a, b, sep='\n')
elif a > b and a < c:
    print(c, b, a, sep='\n')
elif b > a and b < c:
    print(c, a, b, sep='\n')
elif c > a and c < b:
    print(b, a, c, sep='\n')