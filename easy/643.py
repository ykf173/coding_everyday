from typing import List


class Solution:
    def findMaxAverageX(self, nums: List[int], k: int) -> float:
        '''
        暴力法超时
        :param nums:
        :param k:
        :return:
        '''
        lenN = len(nums)
        maxN = float('-inf')
        if lenN == 1:
            return float(nums[0])
        for i in range(lenN):
            for j in range(i + 1, lenN + 1):
                averge = sum(nums[i:j]) / k
                if j - i == k and averge > maxN:
                    # print(j, i, averge)
                    maxN = max(averge, maxN)

        return maxN

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        '''
        :param nums:
        :param k:
        :return:
        '''
        lenN = len(nums)
        maxN = float('-inf')
        left, right = 0, k
        sumN = sum(nums[left:right])
        while right <= lenN:
            maxN = max(maxN, sumN / k)
            if right < lenN:
                sumN = sumN - nums[left] + nums[right]
            right, left = right + 1, left + 1
        return maxN


if __name__ == '__main__':
    s = Solution()
    while 1:
        nums = list(map(int, input().split(',')))
        k = int(input())
        print(s.findMaxAverage(nums, k))

'''
1,12,-5,-6,50,3
4
0,1,1,3,3
4
4,0,4,3,3
5
5
1
'''
