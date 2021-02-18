class Solution:
    def reverse(self, x: int) -> int:
        maxValue = 2 << 30
        if -maxValue <= x < maxValue:
            s = str(x)
            i = len(s) - 1
            flag = False
            while i >= 0 and s[i] == 0:
                i -= 1
                flag = True

            if flag:
                if x < 0:
                    x = -int(s[i - 1:0:-1])
                else:
                    x = int(s[i - 1::-1])
            else:
                if x < 0:
                    x = -int(s[:0:-1])
                else:
                    x = int(s[::-1])
        else:
            x = 0
        if -maxValue <= x < maxValue:
            return x
        else:
            return 0

if __name__ == '__main__':
    s = Solution()
    x0 = 123
    x1 = -123
    x2 = 120
    x3 = 0
    x4 = 1023000000
    x5 = 12300
    x6 = 2147483648
    x10 = 2147483647
    x7 = -2147483648
    x8 = 1200003000000
    x9 = 1200003000


    for i in range(11):
        x = eval('x%s' % i)
        print(s.reverse(x))
