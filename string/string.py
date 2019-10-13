text = input()
count = 1
m = len(text)
string = ''

if m == 1:
    string = string + str(text) + str(count)
else:
    for j in range(0, m-1):
        if text[j] == text[j+1]:
            count += 1
        else:
            string = string + text[j] + str(count)
            count = 1
            
    for k in range(m-1, m):
        if text[-1] == text[-2]:
            string = string + text[k] + str(count)
                        
        else:
            string = string + text[k] + str(count)
            count = 1
            
print(string)


