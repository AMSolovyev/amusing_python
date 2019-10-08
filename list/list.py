lst = [int(i) for i in input('Введите числа:   ').split()]
x = int(input('Введите число:   '))

if x not in lst:
    print('Отсутствует')
else:
    for i in range(len(lst)):
        if lst[i] == x:
            print(i, end=' ')
