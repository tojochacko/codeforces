import sys


def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split(' ')))
    ans = prev = 0
    temp = []

    for i, k in enumerate(a):
        if k > prev:
            ans += 1
        elif k <= prev:
            temp.append(ans)
            ans = 1

        prev = k

    maxval = max(temp, default=0)
    ans = max(ans, maxval)
    print(ans)

main()
