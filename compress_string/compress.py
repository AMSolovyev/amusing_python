string = input()

counter = 1
string = string +'0'
for i in range (0,len(string)-1):
    if string[i] == string[i+1]:
        counter += 1
    else:
        print((string[i]+str(counter)),end='')
        counter = 1