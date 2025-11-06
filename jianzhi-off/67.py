class Solution:
    def strToInt(self, str: str) -> int:
        MAXINT = 2 ** 31 - 1
        str = str.lstrip()
        num, lenS = 0, len(str)
        if not str or str[0].isalpha():
            return 0
        i, signal = 0, 1
        if str[i] == '+':
            i += 1
        elif str[i] == '-':
            i += 1
            signal = -1
        while i < lenS and str[i].isdigit():
            num = num * 10 + int(str[i])
            i += 1
            if num * signal >= MAXINT:
                num = MAXINT
                break
            elif num * signal <= -(MAXINT + 1):
                num = MAXINT + 1
                break
        return num * signal


if __name__ == '__main__':
    s = Solution()
    while 1:
        string = str(input())
        print(s.strToInt(string))
