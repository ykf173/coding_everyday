# from typing import List
import math
import time


def isPrime(num):
    j = 2

    # 方法1： 开方判断
    while j * j <= num:
        if num % j == 0:
            break
        j += 1

    return j >= num ** 0.5


def getPrimeA2B(A: int, B: int) -> list:
    if A == 1:
        A = 2

    if A > B:
        A, B = B, A

    ans = []
    for i in range(A, B + 1):  # 常用做法 ，方法1开始
        if isPrime(i) and i not in ans:
            ans.append(i)

    return ans  # 方法1结束

    # indexes = [True] * B  # 删除法， 方法二开始
    #
    # for i in range(2, B):
    #     if indexes[i]:
    #         ans.append(i)
    #         for j in range(i, B, i):  # 删除i的倍数
    #             indexes[j] = False
    #
    # low, high = 0, len(ans)
    # while low <= high:  # 二分查找A
    #     mid = (low + high) // 2
    #     if A > ans[mid]:
    #         low = mid + 1
    #     elif A < ans[mid]:
    #         high = mid - 1
    #     else:
    #         return ans[mid:]
    # return ans[low:]  # 方法2结束


if __name__ == '__main__':
    while 1:
        A, B = tuple(map(int, input().split()))
        start = time.perf_counter()
        print(getPrimeA2B(A, B))
        print(time.perf_counter() - start)

'''
1 1000
0.0011305000000003673 # 直接查找
0.0002023999999996029 # 删除法

1000 10000
# 直接查找
0.02957169999999998 # 直接查找
0.004494400000000454 # 删除法
'''
