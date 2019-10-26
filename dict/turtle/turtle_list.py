n = int(input())

coordinate_list = []
count = 0
while count!= n:
    data = input().split()
    coordinate_list += data
    count += 1

coordinate1 = 0
coordinate2 = 0    
for i in range(0, len(coordinate_list)):
    if coordinate_list[i] == 'восток':
        coordinate1 += int(coordinate_list[i+1])
 
    elif coordinate_list[i] == 'запад':
        coordinate1 -= int(coordinate_list[i+1])
       
    elif coordinate_list[i] == 'север': 
        coordinate2 += int(coordinate_list[i+1])
       
    elif coordinate_list[i] == 'юг':
        coordinate2 -= int(coordinate_list[i+1])
        
    if coordinate_list[i] == None:
        coordinate1 = 0
        coordinate2 = 0
     
print(coordinate1, coordinate2)
