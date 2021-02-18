from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        size = len(nums)
        left = right = 0
        maxCountOne = 0
        countOne = 0
        while right < size:
            countOne += 1
            if nums[right] != 1:
                countOne -= 1
                left = right + 1
            maxCountOne = max(maxCountOne, right - left + 1)
            right += 1
        return maxCountOne


if __name__ == '__main__':
    s = Solution()
    while 1:
        nums = list(map(int, input().split(',')))
        print(s.findMaxConsecutiveOnes(nums))


'''
1,1,0,1,1,1
1,1,1,1,1
1,0,0,0,1,1,1,1
1,1,1,0,0,0,1,1
0,0,0,0
0,0,0,1
'''
