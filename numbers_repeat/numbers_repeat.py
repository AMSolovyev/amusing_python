n = [int(i) for i in input().split()]
a = sorted(n)
result = []
j = 0
b = 0

for j in a:
    b = a.count(j)
    if b > 1:
       result.append(j)
 
result_without_repeat = list(set(result))
result_string = ' '.join(map(str, result_without_repeat))
print(result_string)