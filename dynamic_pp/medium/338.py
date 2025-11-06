'''
给定一个非负整数num。对于0 ≤ i ≤ num 范围中的每个数字i，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:
输入: 2
输出: [0,1,1]

示例2:
输入: 5
输出: [0,1,1,2,1,2]

'''
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0] * (num + 1)
        highestBit = 0
        for i in range(1, num + 1):
            if not (i & (i - 1)):
                highestBit = i
            ans[i] = ans[i - highestBit] + 1

        return ans

    def countBitsX(self, num: int) -> List[int]:
        ans = []
        for i in range(num + 1):
            ones, x = 0, i
            while x > 0:
                x &= (x - 1)
                ones += 1
            ans.append(ones)
        return ans


if __name__ == '__main__':
    s = Solution()
    while 1:
        num = int(input())
        print(s.countBits(num))
