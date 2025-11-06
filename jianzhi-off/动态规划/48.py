'''
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        if not size:
            return 0
        dp = [1] * size
        stringDict = {s[0]: 0}
        for i in range(1, size):
            if s[i] in stringDict and i - stringDict[s[i]] <= dp[i - 1]:
                dp[i] = i - stringDict[s[i]]
            else:
                dp[i] = dp[i - 1] + 1

            stringDict[s[i]] = i

        return max(dp)


if __name__ == '__main__':
    s = Solution()
    while 1:
        string = input()
        print(s.lengthOfLongestSubstring(string))

'''
abcabcbb
bbbbb
pwwkew
abba
'''
