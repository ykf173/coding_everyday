'''
请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配
'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        动态规划，当前位置dp[i][j]表示匹配s前i个即是s[0~i-1]，p同理。
        :param s:
        :param p:
        :return:
        '''
        sizeRow, sizeCol = len(s), len(p)
        dp = [[False] * (sizeCol + 1) for _ in range(sizeRow + 1)]

        def match(i: int, j: int) -> bool:
            if not i:
                return False
            elif p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        # 数组初始化
        dp[0][0] = True
        # for i in range(1, sizeCol):
        #     if not (i % 2) and p[i] == '*':
        #         dp[0][i] = True

        for i in range(sizeRow + 1):
            for j in range(1, sizeCol + 1):
                if p[j - 1] == '*':
                    dp[i][j] |= dp[i][j - 2]
                    if match(i, j - 1):
                        dp[i][j] |= dp[i - 1][j]
                else:
                    if match(i, j):
                        dp[i][j] |= dp[i - 1][j - 1]

        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    while 1:
        string = input()
        p = input()
        print(s.isMatch(string, p))

'''
aaa
ab*.*
aaaaaa
ab*.*
aa
a*

a*
aaaaaa
a*
aab
c*a*b*
aa
a

[True,True,True,True,True,True, False]
'''
