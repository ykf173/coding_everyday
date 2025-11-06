class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]


if __name__ == '__main__':
    s = Solution()
    while 1:
        string = input()
        k = int(input())
        print(s.reverseLeftWords(string, k))


'''
 s = "abcdefg", k = 2
s = "lrloseumgh", k = 6
'''