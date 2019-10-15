# Find text

Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.
Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода). 
Порядок вывода слов может быть произвольным, каждое уникальное слово﻿ должно выводиться только один раз.

Sample Input 1:

a aa abC aa ac abc bcd a

Sample Output 1:

ac 1
a 2
abc 2
bcd 1
aa 2

Sample Input 2:

a A a

Sample Output 2:

a 3

The script ```find.py``` can help to count the quantity words in the text.

# How to use

```
 python3 find.py
 ```
You can see:
```
As Harry develops through his adolescence, he learns to overcome the problems that face him: magical, social, and emotional, including ordinary teenage challenges such as friendships, infatuation, romantic relationships, schoolwork and exams, anxiety, depression, stress, and the greater test of preparing himself for the confrontation that lies ahead in wizarding Britain's increasingly-violent second wizarding war.
```

You can output like this:
```
relationships, 1
schoolwork 1
problems 1
develops 1
of 1
confrontation 1
adolescence, 1
such 1
for 1
friendships, 1
war 1
in 1
social, 1
himself 1
him: 1
through 1
exams, 1
ahead 1
the 3
greater 1
wizarding 2
emotional, 1
magical, 1
stress, 1
his 1
to 1
second 1
including 1
infatuation, 1
learns 1
overcome 1
face 1
depression, 1
preparing 1
ordinary 1
britain's 1
that 2
teenage 1
harry 1
as 2
increasingly-violent 1
test 1
he 1
anxiety, 1
lies 1
and 3
challenges 1
romantic 1

```
 

You can run the script to use on Linux python or python3 like this:

``` python3 find.py ``` 

On Windows you use similarly.