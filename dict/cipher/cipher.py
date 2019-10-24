initial_alphabet = str(input())
final_alphabet = str(input())
string1 = str(input())
string2 = str(input())

cipher = dict(zip(initial_alphabet, final_alphabet))

str1 = ''
for x in string1:
    for key, value in cipher.items():
        if x == key:
            str1 += value         
print(str1)

str2 = ''
for y in string2:
    for key, value in cipher.items():
        if y == value:
            str2 += key
print(str2)