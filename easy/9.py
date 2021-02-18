from typing import List


class Solution:
    def isPalindrome(self, x: int) -> bool:
        maxValue = 2 ** 31 - 1
        if -(maxValue + 1) <= x <= maxValue:
            s = str(int(x))
            if s == s[::-1]:
                return True
            return False
        else:
            return False


if __name__ == '__main__':
    s = Solution()

    # while 1:
    #     x = int(input())
    #     print(s.isPalindrome(x))

'''
121
0
-121
10
-101
'''

import time

x = [i for i in range(100000)]
s = time.perf_counter()
print(max(x))
print(time.perf_counter() - s)

maxV = -2 ** 31
s = time.perf_counter()
for v in x:
    if v > maxV:
        maxV = v
print(maxV)
print(time.perf_counter() - s)

