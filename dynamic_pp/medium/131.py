'''
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回 s 所有可能的分割方案。
'''
from typing import List



class Solution:
    def partition(self, s: str) -> List[List[str]]:
        size = len(s)
        res, ans = [], []

        @cache
        def isPalindrome(i: int, j: int) -> int:
            if i <= j:
                return 1
            return isPalindrome(i + 1, j - 1) if s[i] == s[j] else -1

        def dfs(i: int):
            if i == size:
                res.append(ans[:])  # 这里复制，不然会动态改变ans，太6了
                return

            for j in range(i, size):
                if isPalindrome(i, j) == 1:
                    ans.append(s[i:j + 1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        isPalindrome.cache_clear()
        return res

    def partitionX(self, s: str) -> List[List[str]]:
        size = len(s)
        dp = [[True] * size for _ in range(size)]

        for i in range(size - 1, -1, -1):
            for j in range(i + 1, size):
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])

        ans = []
        res = []

        def dfs(i: int):
            if i == size:
                res.append(ans[:])  # 这里复制，不然会动态改变ans，太6了
                return

            for j in range(i, size):
                if dp[i][j]:
                    ans.append(s[i:j + 1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)

        return res


if __name__ == '__main__':
    s = Solution()
    while 1:
        string = input()
        print(s.partition(string))
