#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
from typing import List
class Solution:
    def backtrace(self, se, left, right, n, ans):
        if len(se) == 2 * n:
            ans.append(''.join(se))
            se = []
        if left < n:
            se.append('(')
            self.backtrace(se, left+1, right, n, ans)
            se.pop()
        if right < left:
            se.append(')')
            self.backtrace(se, left, right+1, n, ans)
            se.pop()


    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        se, left, right = [], 0, 0
        self.backtrace(se, left, right, n, ans)
        return ans
        

if __name__ == '__main__':    
    s = Solution()
    for i in range(1, 8):
        print(s.generateParenthesis(i))
# @lc code=end

