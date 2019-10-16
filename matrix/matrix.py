data_list = []

while True:
    matrix_list = [i for i in input().split()]
    if matrix_list == ['end']:
        break
    data_list.append(matrix_list)

n = len(data_list)
m = len(data_list[0])

for i in range(n):
    for j in range(m):
        result = int(data_list[i-1][j]) + int(data_list[i+1-n][j]) + \
                 int(data_list[i][j-1]) + int(data_list[i][j+1-m])
        print(result, end=' ')
    print()
