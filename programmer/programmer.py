n = int(input())

if n in range(11, 15) or n in range(111, 115) or \
    n in range(211, 215) or n in range(311, 315) or \
    n in range(411, 415) or n in range(511, 515) or \
    n in range(611, 615) or n in range(711, 715) or \
    n in range(811, 815) or n in range(911, 915):
        print('', n, 'программистов')
elif n == 1 or n % 10 == 1 or n % 100 == 1:
    print(' ', n, 'программист')
elif n % 10 in range(2, 5) or n % 100 in range(2, 5):
    print('', n, 'программиста')
else: 
    print('', n, 'программистов')
