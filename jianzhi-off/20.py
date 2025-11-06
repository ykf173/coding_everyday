import re


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.lstrip().rstrip().replace('E', 'e')
        pattern = '^[\+\-]?((\d+\.?\d*)|(\d*\.?\d+))([e][\+\-]?\d+)?$'
        return not not re.match(pattern, s)

    def isNumberx(self, s: str) -> bool:
        '''
        过不了，很多例子过不了
        :param s:
        :return:
        '''
        start = 0
        s = s.lstrip().rstrip().replace('E', 'e')
        size = len(s)
        flagE = isDicimal = False
        permitList = list(map(str, range(10)))
        permitList.extend(['-', '+', '.', 'e'])
        if not size or s[0] == 'e':  # 空串，错误的指数形式
            return False

        if s[0] in ['-', '+']:
            start += 1

        for i in range(start, size):
            if s[i] == 'e' and i == size - 1:
                return False
            if s[i] == 'e':
                flagE = True
            if flagE and s[i] == '.' or not flagE and s[i] in ['-', '+']:  # 错误的指数
                return False
            if isDicimal and (s[i] == '.' or s[i] == 'e'):  # 错误的小数
                return False
            if s[i] not in permitList:  # 非常规字符， 如a
                return False
            if not isDicimal and s[i] == '.':
                isDicimal = True

        return True


if __name__ == '__main__':
    s = Solution()
    while 1:
        string = input()
        print(s.isNumber(string))

'''
+100
5e2
-123
3.1416
-1E-16
0123
12e
1a3.14
1.2.3
+-5
12e+5.4
1   
    1
0
.
e
e1
1e
.e1
1e+
-.

True,True,True,True,True,True,False,False,False,False,False,True,True,True,False,False,False,False,False,False
'''
