class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        maxlength = 0
        length_s = len(s)
        for i in range(length_s):
            strsub = s[i]
            for j in range(i+1, length_s):
                if s[j] not in strsub and strsub+s[j] in s:
                    strsub += s[j]
            strlen = len(strsub)
            if strlen > maxlength:
                maxlength = strlen
        return maxlength

    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        end = start = 0
        str_len = len(s)
        for i in range(str_len):
            sub = s[start:end]
            if s[i] in sub:
                start += sub.index(s[i]) + 1
                end = i + 1
            else:
                end += 1

            current_length = end - start
            if current_length > maxlength:
                maxlength = current_length

        return maxlength

# while 1:
#     s = input()
#     ans = Solution()
#     print(ans.lengthOfLongestSubstring(s))
