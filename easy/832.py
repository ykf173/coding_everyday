'''
给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。
水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。
反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。
'''
from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        size = len(A)
        for i in range(size):
            A[i] = A[i][::-1]
            A[i] = list(map(lambda x: 1 - x, A[i]))

        return A


if __name__ == '__main__':
    s = Solution()
    while 1:
        nums = list(eval(input()))
        print(s.flipAndInvertImage(nums))

'''
[1,1,0],[1,0,1],[0,0,0]
'''
