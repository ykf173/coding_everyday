from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        sizeRow, sizeCol = len(nums), len(nums[0])
        size = sizeCol * sizeRow
        if size == r * c:
            return nums

        oneDimNums = []
        for i in range(sizeRow):
            for j in range(sizeCol):
                oneDimNums.append(nums[i][j])

        newNums, k = [], 0
        for i in range(r):
            row = []
            for j in range(c):
                row.append(oneDimNums[k])
                k += 1
            newNums.append(row)

        return newNums


if __name__ == '__main__':
    s = Solution()
    while 1:
        nums = input()

'''


'''