#
# @lc app=leetcode.cn id=1502 lang=python3
#
# [1502] 判断能否形成等差数列
#

# @lc code=start
from typing import List

class Solution:
    def sort_jduge(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        n = len(arr)
        for i in range(2, n):
            if arr[i] - arr[i-1] != diff:
                return False
        return True
    
    def math_minmax(self, arr: List[int]) -> bool:
        min_num, max_num = float('inf'), float('-inf')
        n = len(arr)

        for num in arr:
            min_num = min(min_num, num)
            max_num = max(max_num, num)
        
        if (max_num - min_num) % (n-1):
            return False
        
        mean = (max_num - min_num) // (n-1)

        set_arr = set(arr)

        if len(set_arr) == 1:
            return True
        
        for i in range(1, len(set_arr)):
            if min_num + (i * mean) not in set_arr:
                return False
            
        return True



    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:

        return self.math_minmax(arr)


# if __name__ == '__main__':
#     arr = [3,5,1]
#     s = Solution()
#     print(s.canMakeArithmeticProgression(arr))
# @lc code=end

