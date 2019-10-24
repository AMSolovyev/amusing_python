def load_data(in_file):
    input_file = open(in_file) 
    for string in input_file:
        string = string.strip()
    input_file.close()
    return string


def find_numbers(string):
    a_list = []
    length = len(string)
    i = 0
    while i < length:
        string_number = ''
        a = string[i]
        while a.isdigit():
            string_number += a
            i += 1
            if i < length:
                a = string[i]
            else:
                break
        i += 1
        if string_number != '':
            a_list.append(int(string_number))
    return a_list


def find_symbols(string):
    b_list = []
    length = len(string)
    for symbol in string:
        if symbol.isalpha():
            b_list.append(symbol)
    return b_list


def expand_numbers_symbols(a_list, b_list):
    result = []
    for a, b in zip(a_list, b_list):
        result.append(a*b)
    return result


def convert_list_to_string(result):
    result_string = ''.join(result)
    return result_string


def write_result(result_string, out_f):
    out_file = open(out_f, 'w')   
    out_file.write(result_string)
    out_file.close()


if __name__ == '__main__':
    input_file = '/home/linux/Загрузки/dataset_3363_2.txt'
    out_file = '/home/linux/Загрузки/dataset_3363_output.txt'

    loaded = load_data(input_file)
    found_numbers = find_numbers(loaded)
    found_symbols = find_symbols(loaded)
    expanded = expand_numbers_symbols(found_numbers, found_symbols)
    converted = convert_list_to_string(expanded)
    written = write_result(converted, out_file)
