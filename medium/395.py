'''
给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串， 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。
'''


class Solution:
    def dfs(self, s, left, right, k):
        res = 0
        allAlphabet = [0] * 26
        for i in range(left, right + 1):
            allAlphabet[ord(s[i]) - ord('a')] += 1

        split = 0
        for i in range(26):
            if 0 < allAlphabet[i] < k:
                split = i + ord('a')
                break

        if split == 0:
            return right - left + 1

        i, ret = left, 0
        while i <= right:
            while i <= right and ord(s[i]) == split:
                i += 1

            if i > right:
                break

            start = i
            while i <= right and ord(s[i]) != split:
                i += 1

            length = self.dfs(s, start, i - 1, k)
            res = max(res, length)

        return res

    def longestSubstring(self, s: str, k: int) -> int:
        size = len(s)
        return self.dfs(s, 0, size - 1, k)

    def longestSubstringHD(self, s: str, k: int) -> int:
        '''
        统计滑动窗口内每个字符的数量，遍历一遍肯定是增加了时间复杂度，又想到了用最大最小值统计，但是麻烦的是【0-k】的区间这个没法统计，于是又想到了用any,all函数，但是还是不行，只能判断是否为0
        ^-^ 忍不住看了题解，用统计字符种类和个数的方法，加之记录一个当前小于出现了k个个数的字符。这样用字符种类数就能统计了。但是这样只能统计一次，我们使用枚举的方法，全部举出来，自然可以得出每种字符的最大长度。
        :param s:
        :param k:
        :return:
        '''
        ans = 0
        size = len(s)

        for type in range(1, 27):  # 枚举
            left = right = 0
            allAlph = [0] * 26
            kind = less = 0  # kind表示当前窗口字符种类，less表示少于k的种类数
            while right < size:
                index = ord(s[right]) - ord('a')
                allAlph[index] += 1
                if allAlph[index] == 1:
                    less += 1
                    kind += 1

                if allAlph[index] == k:
                    less -= 1

                while kind > type:  # 窗口大小为当前个数的种类
                    index = ord(s[left]) - ord('a')
                    allAlph[index] -= 1
                    if allAlph[index] == k - 1:
                        less += 1

                    if allAlph[index] == 0:
                        less -= 1
                        kind -= 1

                    left += 1
                if not less:
                    ans = max(ans, right - left + 1)
                right += 1

        return ans


if __name__ == '__main__':
    s = Solution()
    while 1:
        string = input()
        k = int(input())
        print(s.longestSubstring(string, k))
'''
aaabb
3
ababbc
2

ans:[3,5]
'''
