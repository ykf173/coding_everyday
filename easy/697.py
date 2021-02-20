import collections
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        numsDict = collections.Counter(nums)
        maxCounter = max(numsDict.values())
        maxValues = {}
        ans, i = 50000, 0
        for key, val in numsDict.items():
            if val == maxCounter:
                maxValues[key] = i
                i += 1

        maxSize = len(maxValues)
        pos = [[] for _ in range(maxSize)]
        for i in range(size):
            if nums[i] in maxValues:
                pos[maxValues[nums[i]]].append(i)

        for i in range(maxSize):
            ans = min(ans, pos[i][-1] - pos[i][0] + 1)

        return ans


if __name__ == '__main__':
    s = Solution()
    while 1:
        nums = list(map(int, input().split(',')))
        print(s.findShortestSubArray(nums))

'''
1, 2, 2, 3, 1
1,2,2,3,1,4,2
1,1,1,1,1,1,1
1,2,3,4,5,6,7
ans: [2, 6, 7, 1]

'''
