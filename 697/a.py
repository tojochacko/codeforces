import sys

t, s, x = map(int, sys.stdin.readline().split())

if x == t:
    print('YES')
elif x < s + t:
    print('NO')
elif x > t:
    remainder = (x-t)%s 
    if remainder<=1:
        print('YES')
    else:
        print('NO')

