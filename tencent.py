from typing import List

# class Solution:
#     def rob(self, nums: [int], ) -> int:
#         def my_rob(nums):
#             cur, pre = 0, 0
#             for num in nums:
#                 cur, pre = max(pre + num, cur), cur
#             return cur
#
#         return max(my_rob(nums[:-1]), my_rob(nums[1:])) if len(nums) != 1 else nums[0]
'''
给定一个整数数组[a1,a2,.....aN]，N个数,现在从里面选择若干数使得他们的和最大，同时满足相邻两数不能同时被选，a1和aN首尾两个也认为是相邻的。

'''


def sumNum(nums, n):
    lenN = len(nums)
    numsDict = {idx: nums[idx] for idx in range(lenN)}
    nums = sorted(numsDict.items(), key=lambda d: d[1])
    j, i = lenN - 1, 0
    res = []
    listNums = []
    while j >= 0 and n > i:
        flag = True
        for num in listNums:
            if abs(nums[j][0] - num) == 1 or abs(nums[j][0] - num) == lenN - 1:
                flag = False
        if flag:
            res.append(nums[j][1])
            listNums.append(nums[j][0])
            i += 1
        j -= 1

    if len(res) < n:
        return -1

    return res


if __name__ == '__main__':

    while 1:
        nums = list(map(int, input().split()))
        n = int(input())
        print(sumNum(nums, n))

'''
1 2 3 4 5 
2

9 1 9 6 0 6 8 6
4

反例
9 7 9 7 0 7 8 7
4
程序输出：[9,9,8,0]
正确答案：[9,9,7,7]

'''
