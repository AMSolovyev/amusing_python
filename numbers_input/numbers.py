n = int(input())

number = 1
if n == 0:
    print(0)
else:
    for i in range(1, n+1):
        print(number, end=' ')
        if 2 * i == number * (number + 1):
            number += 1
