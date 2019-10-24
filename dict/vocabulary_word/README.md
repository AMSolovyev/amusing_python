# Vocabulery word

Простейшая система проверки орфографии основана на использовании списка известных слов. Каждое слово в проверяемом тексте ищется в этом списке и, если такое слово не найдено, оно помечается, как ошибочное.

Напишем подобную систему.

Через стандартный ввод подаётся следующая структура: первой строкой — количество d записей в списке известных слов, после передаётся  d строк с одним словарным словом на строку, затем — количество l строк текста, после чего — l строк текста.

Напишите программу, которая выводит слова из текста, которые не встречаются в словаре. Регистр слов не учитывается. Порядок вывода слов произвольный. Слова, не встречающиеся в словаре, не должны повторяться в выводе программы.

﻿
Sample Input:

3
a
bb
cCc
2
a bb aab aba ccc
c bb aaa

Sample Output:

aab
aba
c
aaa

Sample input 2:

3
a
bb
cCc
3
a bb aab aba ccc
c bb aaa
A BB aaB aBa CcC

Sample output 2:

aba
aBa
aab
aaB
aaa
c
The script ```vocabulery.py``` can help to find vocabulary words in the text.

# How to use

```
 python3 vocabulary.py
 ```
You can see:
```
3
a
bb
cCc
3
a bb aab aba ccc
c bb aaa
A BB aaB aBa CcC

```

You can output like this:
```
aba
aBa
aab
aaB
aaa
c

```
 

You can run the script to use on Linux python or python3 like this:

``` python3 vocabulary.py ``` 

On Windows you use similarly.