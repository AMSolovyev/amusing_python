def create_dict():
    coordinate_dict = {'север': 0, 'запад': 0, 'юг': 0,
                       'восток': 0}
    return coordinate_dict


def input_coordinate(coordinate_dict):
    for _ in range(int(input())):
        key, value = input().split()
        coordinate_dict[key] += int(value)
    return coordinate_dict


def printed_coordinates(coordinate_dict):
    print(coordinate_dict['восток'] - coordinate_dict['запад'],
          coordinate_dict['север'] - coordinate_dict['юг'])


if __name__ == '__main__':
    created = create_dict()
    inputed = input_coordinate(created)
    printed = printed_coordinates(inputed)
