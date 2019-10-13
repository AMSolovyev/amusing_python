n = [int(i) for i in input().split()]
i = 0

if len(n) == 0:
    print(0)
elif len(n) == 1:
    print(n[0])
else:
    for i in range(len(n)):
        if i != len(n) - 1:
            print((n[i-1] + n[i+1]), end=' ')
            i += 1
        else:
            print(n[i-1] +n[0], end=' ')