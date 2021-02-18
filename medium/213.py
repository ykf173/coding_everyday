from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [0] * size
        if not nums:
            return 0
        if size == 1:
            return nums[0]

        dp[1:3] = nums[1], max(nums[1:3])
        for i in range(3, size):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        ans = dp[size - 1]
        dp[:2] = nums[0], max(nums[0:2])
        for i in range(2, size - 1):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return max(ans, dp[size - 2])


if __name__ == '__main__':
    s = Solution()
    while 1:
        nums = list(map(int, input().split(',')))
        print(s.rob(nums))

'''
2,3,2
1,2,3,1
0
1,7,9,2
'''
