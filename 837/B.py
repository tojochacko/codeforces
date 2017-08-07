#! /usr/bin/python3
import sys

def verifyFlag(flagList, row, column):
    if row%3 != 0:
        return False

    q = row // 3 #since there are 3 equal parts
    u = [flagList[(0 * q)], flagList[(1 * q)], flagList[(2 * q)]]
    us = set(u) #removes duplicates

    patternToMatch = set()
    for color in ['R', 'G', 'B']:
        patternToMatch.add(color*column)

    if us != patternToMatch:
        return False

    for i,row in enumerate(flagList):
        if row != u[i//q]:
            return False
    return True

def main():
    n, m = map(int,sys.stdin.readline().split())

    #get the horizontal columns
    a = []
    for i in range(n):
        a.append(sys.stdin.readline().rstrip())

    #get the vertical columns
    b = []
    for i in range(m):
        temp = ''
        for j in range(n):
            temp += a[j][i]
        b.append(temp)

    rv1 = verifyFlag(a,n,m)
    rv2 = verifyFlag(b,m,n)

    if rv1 or rv2:
        print('YES')
    else:
        print('NO')

main()