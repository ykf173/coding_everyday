#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
import math
class Solution:
    # ans = [0, 1, 1, 1]

    def iterative_mothod(self, x):
        start = 1
        if 0 < x < self.ans.__len__():
            return self.ans[x]
        else:
            start = self.ans[-1]
        
        for i in range(start, x):
            cur_val = i * i - x
            if cur_val == 0:
                return i
            if cur_val > 0:
                return i - 1
        return x
    
    def exp_log(self, x):
        if not x:
            return x
        ans = int(math.exp(0.5 * math.log(x)))
        return ans + 1 if (ans + 1) * (ans + 1) <= x else ans

    def mySqrt(self, x: int) -> int:
        return self.exp_log(x)

if __name__ == '__main__':  
    s = Solution()
    for i in range(11):
        print(i, s.mySqrt(i))

# @lc code=end

