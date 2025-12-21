#
# @lc app=leetcode.cn id=955 lang=python3
#
# [955] 删列造序 II
#

# @lc code=start
from typing import List

class Solution:
    def baoli(self, strs: List[str]) -> int:
        def is_order(s): # O(m*n)
            return all(s[i+1] >= s[i] for i in range(len(s) - 1))
        
        ans = 0
        n = len(strs)
        cur = [''] * n
        for col in zip(*strs): # O(m*n*n)
            col2 = cur[:]
            for i in range(n):
                col2[i] += col[i]
            
            if is_order(col2):
                cur = col2
            else:
                ans += 1

        return ans
    
    def sota(self, strs: List[str]) -> int: # 字符串比较
        def is_order(i):
            return all(lt[j] or strs[j][i] <= strs[j+1][i] for j in range(m-1))
        
        ans = 0
        m, n = len(strs), len(strs[0])
        lt = [False] * (m-1) # cur[j] is True, col[j+1] > col[j]
        for i in range(n): # O(m*n)
            # lt[j] = False # 下面的小于上面的
            if is_order(i):
                for j in range(m-1):
                    if not lt[j] and strs[j][i] < strs[j+1][i]:
                        lt[j] = True
            else:
                ans += 1

        return ans

    def minDeletionSize(self, strs: List[str]) -> int:
        # return self.baoli(strs)
        return self.sota(strs)


if __name__ == '__main__':
    strs = ["xga","xfb","yfa"]
    strs = ["ca","bb","ac"]
    s = Solution()
    print(s.minDeletionSize(strs))
                    
# @lc code=end

