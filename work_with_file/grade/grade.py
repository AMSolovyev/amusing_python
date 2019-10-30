def opened_data(path, path_out):
    result_one = 0
    result_two = 0
    result_three = 0
    count = 0
    with open(path) as file_input:
        for text in file_input:
            text = text.strip()
            text = text.split(';')
            result = (int(text[1]) + int(text[2]) + int(text[3]))/3
            result_one += int(text[1])
            result_two += int(text[2])
            result_three += int(text[3])
            count += 1
            print(result)
        result_one = result_one / count
        result_two = result_two / count
        result_three = result_three / count
        print(result_one, result_two, result_three)


if __name__ == '__main__':

    path = '/home/linux/Загрузки/dataset_3363_4.txt'
    path_out = '/home/linux/Загрузки/result.txt'

    opened = opened_data(path, path_out)

    