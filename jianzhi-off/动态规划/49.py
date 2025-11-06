'''
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
'''
from sortedcontainers import SortedList

N = 1690


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i2 = i3 = i5 = 0
        dp = [1]
        for i in range(1, N):
            urly = min(dp[i2] * 2, dp[i3] * 3, dp[i5] * 5)
            dp.append(urly)

            if urly == dp[i2] * 2:
                i2 += 1
            if urly == dp[i3] * 3:
                i3 += 1
            if urly == dp[i5] * 5:
                i5 += 1

        return dp[n - 1]

    def nthUglyNumberx(self, n: int) -> int:
        dp = SortedList([1, 2, 3, 5])
        minIndex = 1

        for i in range(N):
            for j in [2, 3, 5]:
                if dp[minIndex] * j not in dp:
                    dp.add(dp[minIndex] * j)
            minIndex += 1
        return dp[n - 1]


if __name__ == '__main__':
    s = Solution()
    while 1:
        n = int(input())
        print(s.nthUglyNumber(n))
