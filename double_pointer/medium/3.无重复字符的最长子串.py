#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = defaultdict(int)
        n = len(s)
        max_len = 0
        i = j = 0

        for j in range(n):
            i = max(i, visited[s[j]])
            visited[s[j]] = j + 1
            max_len = max(max_len, j - i + 1)

        return max_len
# @lc code=end

