def get_file(in_file):
    data_file = open(in_file)
    for string in data_file:
        string = string.strip()
        string = string.split(';')
        print(string)   
        return string        
    data_file.close()
    

#def count_average_grades(string):
 #   average_grades = 0
 #   for i in range(1, len(string)):     
 #       average_grades = sum([grade[i] for [*grade] in string])/len(string)
 #       return average_grades
 

def printed_results(string):
    print(string, sep='\n')



if __name__ == '__main__':
    input_file = '/home/linux/Загрузки/dataset_3363_4.txt'

    loaded = get_file(input_file)
    #counted_average_grades = count_average_grades(loaded) 
    printed = printed_results(loaded)