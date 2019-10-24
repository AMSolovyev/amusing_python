# Find repeat

Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.

Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

В качестве ответа укажите вывод программы, а не саму программу.

Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:

abc a bCd bC AbC BC BCD bcd ABC


Sample Output:

abc 3


The script ```find_repeat.py``` can help to find repeats in the text.

# How to use

```
 python3 find_repeat.py
 ```
You can see:
```
abc a bCd bC AbC BC BCD bcd ABC

```

You can output like this:
```
abc 3

```
 

You can run the script to use on Linux python or python3 like this:

``` python3 find_repeat.py ``` 

On Windows you use similarly.