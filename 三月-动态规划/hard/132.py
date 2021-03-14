'''
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
返回符合要求的 最少分割次数 。


示例 1：
输入：s = "aab"
输出：1
解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。

示例 2：
输入：s = "a"
输出：0

示例 3：
输入：s = "ab"
输出：1

提示：
1 <= s.length <= 2000
s 仅由小写英文字母组成
'''

class Solution:
    def minCut(self, s: str) -> int:
        size = len(s)

        dp = [[True] * size for _ in range(size)]
        for i in range(size - 1, -1, -1):
            for j in range(i + 1, size):
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])

        res = [float('inf')] * size   # res[i]表示是s[0:i]的最少切分次数
        for i in range(size):
            if dp[0][i]:
                res[i] = 0
            else:
                for j in range(i):
                    if dp[j + 1][i]:
                        res[i] = min(res[i], res[j] + 1)

        return res[size - 1]


if __name__ == '__main__':
    s = Solution()
    while 1:
        string = input()
        print(s.minCut(string))
