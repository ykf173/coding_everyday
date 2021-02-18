from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        lenN = len(nums)
        dp = [0] * lenN
        dp[0] = nums[0]
        for i in range(1, lenN):
            dp[i] = dp[i - 1] + nums[i] if dp[i - 1] > 0 else nums[i]
        return max(dp)


if __name__ == '__main__':
    s = Solution()
    while 1:
        nums = list(map(int, input().split(',')))
        print(s.maxSubArray(nums))

'''
-2,1,-3,4,-1,2,1,-5,4
6
'''
