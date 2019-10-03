#!/usr/bin/env python
# -*- coding:utf-8 -*-
def number_inputing():
    a = int(input('Введите количество чисел: '))
    b = list(map(int, input('Введите числа: ').split()))
    return a, b

def number_sum(a, b):
    print(sum([x for x in b]))


if __name__ == '__main__':
	m, n = number_inputing()
	number_sum(m, n)


