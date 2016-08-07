import sys

#
# def is_pow_of_two(n):
#     while n != 1:
#         if n % 2 != 0:
#             return False
#         else:
#             n /= 2
#
#     return True


def main():
    ans = 0
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split(' ')))
    store = {}
    power = {}

    for k, v in enumerate(a):
        store[v] = store.get(v, 0) + 1

    power[1] = 2
    for i in range(2, 32):
        power[i] = power[i-1]*2

    for k, v in enumerate(a):
        store[v] -= 1
        for i in range(1, 32):
            if power[i] > v and (power[i]-v) in store:
                ans += store[power[i]-v]

    # for i, k in enumerate(a):
    #     var1 = k
    #     for j, l in enumerate(a):
    #         if i < j:
    #             var2 = l
    #             sum_of_var = var1 + var2
    #             if sum_of_var in store:
    #                 ans += 1
    #             else:
    #                 if is_pow_of_two(sum_of_var):
    #                     store.append(sum_of_var)
    #                     ans += 1

    return ans

answer = main()
print(answer)
