def create_dict():
    dict_height = {i: [0, 0] for i in range(1, 12)}                   
    return dict_height


def write_in(dict_height, path):
    with open(path) as file_in:
        for text in file_in:
            dict_height[int(text.split()[0])][0] += int(text.split()[2])
            dict_height[int(text.split()[0])][1] += 1
    return dict_height


def printed_dict(dict_height):
    for key, value in dict_height.items():
        if value == [0, 0]:
            print(key, '-')
        else:
            print(key, value[0] / value[1])


if __name__ == '__main__':
    path = 'dataset_3380_5.txt'

    created = create_dict()
    written = write_in(created, path)
    printed = printed_dict(written)
