import pandas


data = pandas.read_csv('dataset_3363_4.txt', sep=';',
                       names=[
                              'Фамилия', 'Математика', 'Физика',
                              'Русский язык'
                       ])

mathematics = data['Математика'].mean()
phisics = data['Физика'].mean()
russian = data['Русский язык'].mean()

data['Среднее оценка ученика'] = (data['Математика'] + data['Физика'] +
                                  data['Русский язык']) / 3
mean_greade = data['Среднее оценка ученика']

with open('result.txt', 'w') as file:
    for value in mean_greade:
        file.write(str(value)+'\n')
    file.write(str(mathematics) + ' ' + str(phisics) + ' ' + str(russian))