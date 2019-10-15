# Compress symbols 

Предложи использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.
Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.

Sample Input 1:

aaaabbcaa

Sample Output 1:

a4b2c1a2

Sample Input 2:

abc
Sample Output 2:

a1b1c1

The script ```compress.py``` can compress the symbols.


# How to use

```
 python3 compress.py
 ```
You can input:
```
aaaabbcaa

```

You can output like this:
```
a4b2c1a2

```
 

You can run the script to use on Linux python or python3 like this:

``` python3 compress.py ``` 

On Windows you use similarly.