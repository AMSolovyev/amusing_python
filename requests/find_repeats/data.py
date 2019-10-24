import requests


def load_data(path):
	response = requests.get(path)
	data = response.text.splitlines()
	return data


def work_to_text(data):
	length = len(data)
	return length


def printer_result(length):
	print(length)


if __name__ == '__main__':
	path = 'https://stepic.org/media/attachments/course67/3.6.2/349.txt'
	
	loaded_data = load_data(path)
	worked = work_to_text(loaded_data)
	printed_result = printer_result(worked)