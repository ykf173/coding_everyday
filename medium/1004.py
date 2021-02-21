from typing import List

'''
leetcode 1004 最大连续1的个数
题目描述：
给定一个由若干0和1组成的数组A,我们最多可以将 K 个值从 0 变成 1。
返回仅包含 1 的最长（连续）子数组的长度。
'''


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        size = len(A)
        right = left = 0
        maxLen, count0, count1 = 0, 0, 0
        while right < size:
            count1 = right - left + 1
            if not A[right]:
                count0 += 1
            if count0 > K:
                count1 -= 1
                count0 = count0 if A[left] else count0 - 1
                left += 1

                maxLen = max(maxLen, count1)
            right += 1


        return max(maxLen, right - left)


if __name__ == '__main__':
    s = Solution()
    while 1:
        A = list(map(int, input().split(',')))
        K = int(input())
        print(s.longestOnes(A, K))

'''
1,1,0
2
0,0,0,1,0,1,1,0
3
0,0,0,0
1
1,1,1,1,1,1
5
1,1,1,0,0,0,1,1,1,1,0
2
0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1
3
1,1,1,0,0,0,1,1,1,1
0

ans：[3,6,1,6,6,10]
'''
