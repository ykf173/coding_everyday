'''
给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度。



示例1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
    请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。


提示：

0 <= s.length <= 5 * 104
s由英文字母、数字、符号和空格组成
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lens = len(s)
        char_set = set()
        max_len = 0
        i = j = 0
        while j < lens:
            while s[j] in char_set:
                max_len = max(max_len, j - i + 1)
                i += 1
                char_set.add(s[i])

            else:
                j += 1

        return max_len


if __name__ == '__main__':
    chs = [
        "abcabcbb",
        "bbbbb",
        "pwwkew"
    ]
    s = Solution()
    for ch in chs:
        print(s.lengthOfLongestSubstring(ch))
