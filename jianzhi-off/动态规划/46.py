'''
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
'''


class Solution:
    def translateNum(self, num: int) -> int:
        if num < 10:
            return 1

        strNum = str(num)
        size = len(strNum)
        kinds = [1]
        if 9 < 10 * int(strNum[0]) + int(strNum[1]) < 26:
            kinds.append(2)
        else:
            kinds.append(1)

        for i in range(2, size):
            curValue = 10 * int(strNum[i - 1]) + int(strNum[i])
            if 9 < curValue < 26:
                kinds.append(kinds[i - 1] + kinds[i - 2])
            else:
                kinds.append(kinds[i - 1])

        return kinds[-1]


if __name__ == '__main__':
    s = Solution()
    while 1:
        num = int(input())
        print(s.translateNum(num))

'''
12258
0000
1234
25
26
506
1068385902

ans:[5,1,3,2,2,1,1,2]
'''
