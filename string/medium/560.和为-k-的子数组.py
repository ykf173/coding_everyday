#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start
from typing import List
from collections import defaultdict

class Solution:
    def per_sum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dic_cnt = defaultdict(int)
        pre_sum = [0] * (n+1)

        res = 0
        for i in range(1, n+1):
            pre_sum[i] = pre_sum[i-1] + nums[i-1]
        
        # for i in range(1, n+1):
        #     pre_sum[i] = pre_sum[i-1] + nums[i-1]

        for pre in pre_sum:
            res += dic_cnt[pre - k] # 取前缀
            dic_cnt[pre] += 1 # 放s[i]求和

        # res = dic_cnt[pre - k]
        return res

    def subarraySum(self, nums: List[int], k: int) -> int:
        return self.per_sum(nums, k)


# @lc code=end




if __name__ == "__main__":


    s = Solution()
    nums = [1,1,1]
    k = 2
    nums = [1,2,3]
    k = 3

    nums = [1,1,-1,1,-1]
    k=1
    # nums = [1]
    # k = 1

    # nums = [-1,-1,1]
    # k = 1
    print(s.subarraySum(nums, k))
