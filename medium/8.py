import re


class Solution:
    def myAtoi(self, s: str) -> int:
        maxValue = 2 ** 31
        i = 0
        s = s.lstrip()

        if s == '':  # 异常处理空字符串
            return 0

        sign = 1
        if s[0] == '-':
            sign = -1
            i = 1

        if s[0] == '+':
            i = 1

        start = i
        while i < len(s) and '0' <= s[i] <= '9':
            i += 1
        if start == i:
            return 0

        x = sign * int(s[start:i])
        if -maxValue <= x < maxValue:
            return x
        elif x < -maxValue:
            return -maxValue
        else:
            return maxValue - 1


class Solution2:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        num = re.search('^[\+\-]?\d+', s)
        if num:
            num = num.span()
            return max(min(int(s[num[0]:num[1]]), 2 ** 31 - 1), -2 ** 31)
        else:
            return 0

class Solution:
    class Solution2:
        def myAtoi(self, s: str) -> int:
            '''
            1. s.lstrip() 删除字符串最左端空格字符
            2. 正则表达式 ^[\+\-]?\d+， ^匹配字符串开头字符， [\+\-]？匹配0个或者一个中括号中的字符，\d表示数字字符，+表示至少一个
            3. re.findall返回列表, 前面的*是解包的意思，由于取第一个数字串，故列表中只有一个元素，解包即去掉列表转为字符串，但是这里不能取
            4. int(*re.findall)，找到即返回数字，否则就是0
            5. 处理越界，先与最大取最小值，在与最小值取最大值
            :param s:
            :return:
            '''
            return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2 ** 31 - 1), -2 ** 31)


MAX_SIGNED = 2 ** 31 - 1
MIN_SIGNED = - (MAX_SIGNED + 1)


class DFA:
    def __init__(self):
        '''
        绘制状态转移表
        state为当前状态，初始为start
        sign为正负号标记
        ans为最终答案
        state_table为状态转移表
        '''
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.state_table = {
            'start': ['start', 'signed', 'in_num', 'end'],
            'signed': ['end', 'end', 'in_num', 'end'],
            'in_num': ['end', 'end', 'in_num', 'end'],
            'end': ['end', 'end', 'end', 'end']
        }

    def get_col_state(self, char):
        '''
        对应每个列表下标
        :param char:
        :return:
        '''
        if char.isspace():
            return 0
        elif char == '-' or char == '+':
            return 1
        elif char.isdigit():
            return 2
        else:
            return 3

    def get_current_state(self, char):

        self.state = self.state_table[self.state][self.get_col_state(char)]
        if self.state == 'in_num':
            self.ans = self.ans * 10 + int(char)
            self.ans = min(self.ans, MAX_SIGNED) if self.sign == 1 else min(self.ans, -MIN_SIGNED)
        if self.state == 'signed':
            self.sign = -1 if char == '-' else 1


class Solution3:
    def myAtoi(self, s: str) -> int:
        dfa = DFA()
        for c in s:
            dfa.get_current_state(c)
        return dfa.sign * dfa.ans


if __name__ == '__main__':
    s = Solution()
    # s2 = Solution2()
    s3 = Solution3()
    while 1:
        x = input()
        print(s.myAtoi(x))
        # print(s1.myAtoi(x))

'''
42
-42
0012
-0012
-91283472332
91283472332
words and 987
   -42
    870 lksadjf
    9087
    
    -
+1
   +123
   +234 jl;ksda
+-12
-+12
'''

import time

s = time.perf_counter()
print(2 ** 31)
print(time.perf_counter() - s)



