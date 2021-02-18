'''
打家劫舍
'''

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        lenN = len(nums)
        dp = [0] * lenN
        if lenN == 0:
            return 0
        if lenN == 1:
            return nums[0]
        dp[:2] = nums[0], max(nums[0], nums[1])
        for i in range(2, lenN):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[lenN - 1]

    def robX(self, nums: List[int]) -> int:
        '''
        用例2,3,2过不了
        2,3,2,1,2
        这种用例都过不了
        因为该方法排序，只能注重值，未关注数量
        所以需要用到动态规划方法
        :param nums:
        :return:
        '''
        numsDict = {idx: num for idx, num in enumerate(nums)}
        sotedNums = sorted(numsDict.items(), key=lambda d: d[1], reverse=True)
        setIdxs = set()
        lenN = len(nums)
        ans = 0
        for i in range(lenN):
            flag = True
            for idx in setIdxs:
                if not flag:
                    break
                if abs(sotedNums[i][0] - idx) == 1:
                    flag = False
            if flag:
                setIdxs.add(sotedNums[i][0])
                ans += sotedNums[i][1]
                # print(sotedNums[i][1])
        return ans


if __name__ == '__main__':
    s = Solution()
    while 1:
        nums = list(map(int, input().split(',')))
        print(s.rob(nums))

'''
1,2,3,1
2,7,9,3,1
2,3,2
2,1,1,2
'''
