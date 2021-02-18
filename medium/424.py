class Solution:
    def characterReplacementX(self, s: str, k: int) -> int:
        '''
        顺序查询，解决不了该问题
        :param s:
        :param k:
        :return:
        '''
        maxSNum = 0
        lenS = len(s)
        if k >= lenS:
            return lenS

        for i in range(lenS):
            j = i + 1
            diffNum = k
            while j < lenS:
                if diffNum > 0 and s[i] != s[j]:
                    diffNum -= 1
                    j += 1

                elif s[i] == s[j]:
                    j += 1

                if j >= lenS or (j < lenS and diffNum <= 0 and s[i] != s[j]):
                    maxSNum = max(maxSNum, j - i)
                    break

        return maxSNum

    def characterReplacement(self, s: str, k: int) -> int:
        '''
        有种方法，可以很好的解决该问题，重要的是审题，该题限定出现的字符只有大写字母，所以可以对应数组下标，构建哈希表
        '''
        lenS = len(s)
        letters = [0] * lenS
        maxNum = 0
        left = right = 0
        A = ord('A')

        while right < lenS:
            letters[ord(s[right]) - A] += 1
            maxNum = max(maxNum, letters[ord(s[right]) - A])
            if right - left + 1 - maxNum > k:
                letters[ord(s[left]) - A] -= 1
                left += 1
            right += 1
        return right - left


if __name__ == '__main__':
    s = Solution()
    while 1:
        string = input()
        k = int(input())
        print(s.characterReplacement(string, k))

'''
ABAB
2

AABABBA
1

ABCDEFAAA
0

ABCDAABCBBBA
2

ABA
6

ABC
10

AAA
0

AABA
0
'''
