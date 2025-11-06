from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        setNums = set()
        for num in nums:
            lenSetNums = len(setNums)
            setNums.add(num)
            if len(setNums) == lenSetNums:
                return num
        return nums[0]


if __name__ == '__main__':
    s = Solution()
    while 1:
        nums = list(map(int, input().split(',')))
        print(s.findRepeatNumber(nums))


'''
2,3,1,0,2,5,3
1,2,3,4,4,5,6,7
1,2,3,4,5,6
'''