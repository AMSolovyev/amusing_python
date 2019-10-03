n = int(input('Input a number:  '))
a = list(map(int, input('Input numbers quantity:    ').split()))


result = []
divisor_quantity = 1

for k in range(n):
    dev = 0
    a[k] = int(a[k])
    for l in range(1, a[k]+1):
        if a[k] % l == 0:
            dev += 1
    if dev == divisor_quantity and a[k] not in result:
        result.append(a[k])
    if dev > divisor_quantity:
        divisor_quantity = dev
        result = [a[k]]
for k in range(len(result)):
    print(result[k])