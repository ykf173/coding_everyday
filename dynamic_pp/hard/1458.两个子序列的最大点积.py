#
# @lc app=leetcode.cn id=1458 lang=python3
#
# [1458] 两个子序列的最大点积
#

# @lc code=start
from typing import List
class Solution:
    def dp_method(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        ng = float('-inf')
        dk = [[ng] * (n+1)for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                cur_val = nums1[i-1] * nums2[j-1]
                dk[i][j] = max(dk[i][j-1], dk[i-1][j], dk[i-1][j-1] + cur_val, cur_val)
        return dk[-1][-1]

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        return self.dp_method(nums1, nums2)
    
if __name__ == '__main__':
    nums1 = [2,1,-2,5]
    nums2 = [3,0,-6]

    nums1 = [-3,-8,3,-10,1,3,9]
    nums2 = [9,2,3,7,-9,1,-8,5,-1,-1]

    s = Solution()
    print(s.maxDotProduct(nums1, nums2))
        
# @lc code=end

