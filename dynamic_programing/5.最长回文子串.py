#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def mid_sta(self, s):
        n = len(s)
        start, end = 0, 0
        for i in range(n):
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            if end - start < right - left - 2: # 匹配的时候多走了一步，现在往回退一步
                start, end = left + 1, right - 1

            left, right = i, i+1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            if end - start < right - left - 2:
                start, end = left + 1, right - 1

        return s[start: end+1]

    def dynamic_programing(self, s):
        n = len(s)

        dp = [[False] * n for _ in range(n)]
        max_str = ''

        for i in range(n):
            for j in range(n):
                if i == j:
                    dp[i][j] = True
                    continue
                elif i - 1 > 0 and j - 1 < 0 and:
                    dp[i][j] = dp[i-1][j-1] and s[i] == s[j]
                else:
                    dp[i][j] = 
                


    def longestPalindrome(self, s: str) -> str:
        return self.mid_sta(s)
        

if __name__ == '__main__':
    st = 'babad'
    st = 'bbaa'
    st = 'b'
    st = 'abcd'
    s =  Solution()
    print(s.longestPalindrome(st))
# @lc code=end

