from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count, size, curNumber = 0, len(nums), nums[0]
        for i in range(1, size):
            if nums[i - 1] > nums[i]:
                count += 1
                if i > 1 and nums[i - 2] > nums[i]:
                    nums[i] = nums[i-1]
                else:
                    nums[i-1] = nums[i]
            if count > 1:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    while 1:
        nums = list(map(int, input().split(',')))
        print(s.checkPossibility(nums))

''''
4,2,3
4,2,1
2,2,2
3,4,2,3
-1,4,2,3
5,7,1,8
'''
