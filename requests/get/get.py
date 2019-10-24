import requests


def get_file(path, filename):
    while filename:
        print(filename)
        response = requests.get(path+filename)
        filename = None if response.text.startswith('We') else response.text
    print(response.text)


if __name__ == '__main__':
    path = 'https://stepic.org/media/attachments/course67/3.6.3/'
    filename = '699991.txt'

    get_file(path, filename)
