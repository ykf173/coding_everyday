#
# @lc app=leetcode.cn id=3075 lang=python3
#
# [3075] 幸福值最大化的选择方案
#

# @lc code=start
from typing import List

class Solution:
    def dp(self, happiness: List[int], k: int) -> int:
        def sift_down(i, n):
            while True:
                largest = i
                left = 2 * i + 1
                right = left + 1
                if left < n and happiness[left] < happiness[largest]:
                    largest = left
                if right < n and happiness[right] < happiness[largest]:
                    largest = right

                if largest == i:
                    break
                
                happiness[i], happiness[largest] = happiness[largest], happiness[i]
                i = largest
        
        n = len(happiness)
        for i in range(k // 2 - 1, -1, -1):
            sift_down(i, k)
        
        ans = 0
        for i in range(k, n):
            if happiness[0] < happiness[i]:
                happiness[0], happiness[i] = happiness[i], happiness[0]
                sift_down(0, k)

        happiness[:k] = sorted(happiness[:k], reverse=True)
        cnt = 0
        for i in range(k):
            if happiness[i] > cnt:
                ans += happiness[i] - cnt
            cnt += 1
        
        return ans
    
    def sort_method(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        ans = 0
        for i in range(k):
            ans += max(happiness[i] - i, 0)
        return ans

    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # return self.dp(happiness, k)
        return self.sort_method(happiness, k)
    
    
if __name__ == '__main__':
    s = Solution()
    h = [5,4,3,14,1]; k = 3
    h = [1,2,3]; k = 2
    h = [1,1,1,1]; k = 3


    print(s.maximumHappinessSum(h, k))

        
# @lc code=end

