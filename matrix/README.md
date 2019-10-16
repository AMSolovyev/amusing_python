# Matrix

Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся строкой, содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.

Sample Input 1:

9 5 3
0 7 -1
-5 2 9
end

Sample Output 1:

3 21 22
10 6 19
20 16 -1

Sample Input 2:

1
end

Sample Output 2:

4

The script ```matrix.py``` can count a matrix.

# How to use

```
 python3 matrix.py
 ```
You can input:
```
9 5 3
0 7 -1
-5 2 9
end
```

You can output like this:
```
3 21 22
10 6 19
20 16 -1
```
 
You can run the script to use on Linux python or python3 like this:

``` python3 matrix.py ``` 

On Windows you use similarly.

``` 
Help

    j-1|  j  |j+1|
i-1|   |     |   |

i  |   |     |   |

i+1|   |     |   |

```