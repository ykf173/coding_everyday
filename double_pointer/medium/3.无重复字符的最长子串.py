#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring_pointer(self, s: str) -> int:
        n = len(s)

        if n < 1:
            return n
            
        i, j = 0, 1
        max_len = 1
        while j < n and i < n:
            if s[j] not in s[i:j]:
                j += 1
            else:
                i += 1
            max_len = max(max_len, j - i)

    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        if n < 1:
            return n

        dp = [1] * n
        i, j = 0, 1
        max_len = 1
        for i in range(1, n):
            if s[j] not in s[i:j]:
                dp[i] = dp[i-1] + 1
            else:
                dp

        return max_len

if __name__ == "__main__":
    a = "abcabcbb"
    # a = "bbbbb"
    # a = "pwwkew"
    # a = '123415'

    s = Solution()
    print(s.lengthOfLongestSubstring(a))
    


# @lc code=end

