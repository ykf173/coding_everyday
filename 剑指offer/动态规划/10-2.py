'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
'''


class Solution:
    def numWays(self, n: int) -> int:
        front = post = 1
        for _ in range(n):
            front, post = post, (front + post) % int(1e9 + 7)
        return front


if __name__ == '__main__':
    s = Solution()
    while 1:
        n = int(input())
        print(s.numWays(n))
