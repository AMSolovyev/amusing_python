n = []
while True:
  b = int(input())
  n.append(b)
  if sum(int(i) for i in n) == 0:
    break
print(sum(i**2 for i in n))
