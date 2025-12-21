#
# @lc app=leetcode.cn id=944 lang=python3
#
# [944] 删列造序
#

# @lc code=start
from typing import List

class Solution:

    def baoli(self, strs: List[str]) -> int:
        # del_cols = set()
        ans = 0
        m, n = len(strs), len(strs[0])
        for i in range(n):
            src = 'a'
            for j in range(m):
                if ans == n:
                    return n
                if strs[j][i] < src:
                    # del_cols.add(i)
                    ans += 1
                    break
                # print(src, strs[j][i], del_cols)
                src = strs[j][i]

        return ans
    

    def minDeletionSize(self, strs: List[str]) -> int:
        self.baoli(strs)
        
if __name__ == '__main__':
    strs = ["zyx","wvu","tsr"]
    s = Solution()

    print(s.minDeletionSize(strs))
# @lc code=end

