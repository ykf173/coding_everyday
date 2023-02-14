# 给你一个字符串 s，找到 s 中最长的回文子串。
# 
# 如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 示例 2：
# 
# 输入：s = "cbbd"
# 输出："bb"
# 
# 
# 提示：
# 
# 1 <= s.length <= 1000
# s 仅由数字和英文字母组成

# ac
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         len_s = len(s)
#
#         i = 0
#         j = 1
#         max_s = s[0]
#         while j < len_s:
#
#             cur_s = s[j]
#             l, r = j - 1, j + 1
#             while r < len_s and l >= 0 and s[l] == s[r]:
#                 cur_s = s[l] + cur_s + s[r]
#                 l -= 1
#                 r += 1
#             max_s = cur_s if len(cur_s) > len(max_s) else max_s
#
#             if s[i] == s[j]:
#                 cur_s = s[i] + s[j]
#                 l, r = i - 1, j + 1
#                 while l >= 0 and r < len_s and s[r] == s[l]:
#                     cur_s = s[l] + cur_s + s[r]
#                     l -= 1
#                     r += 1
#                 max_s = cur_s if len(cur_s) > len(max_s) else max_s
#             i += 1
#             j += 1
#
#         return max_s

class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        if len_s < 2:
            return s
        max_len = 1
        begin = 0
        dp = [[False if i != j else True for i in range(len_s)] for j in range(len_s)]

        for l in range(2, len_s + 1):  # 枚举的是子串长度
            for i in range(len_s):
                j = l + i - 1  # j是右边界，i是左边界
                if j >= len_s:
                    break
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and l > max_len:
                    begin = i
                    max_len = l
        return s[begin: max_len + begin]


if __name__ == '__main__':
    s = Solution()

    inputs = [
        "babad",
        "cbbd",
        'xxxxxx',
        'xxxxx',
        'abcd258852'
    ]

    for input in inputs:
        print(s.longestPalindrome(input))
