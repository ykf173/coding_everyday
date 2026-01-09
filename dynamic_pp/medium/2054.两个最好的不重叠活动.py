#
# @lc app=leetcode.cn id=2054 lang=python3
#
# [2054] 两个最好的不重叠活动
#

# @lc code=start
#
# @lc app=leetcode.cn id=2054 lang=python3
#
# [2054] 两个最好的不重叠活动
#

# @lc code=start
from typing import List
class Solution:
    def baoli(self, events: List[List[int]]) -> int: # time out
        n = len(events)
        # dp = [[0] * n for _ in range(n)]
        ans = 0
        for i in range(n):
            ans = max(ans, events[i][-1])
            for j in range(i+1, n):
                if events[j][0] > events[i][1] or events[j][1] < events[i][0]:
                    ans = max(ans, events[j][-1] + events[i][-1], )
        return ans
    
    def sort_bi_search(self, events: List[List[int]]) -> int: # time out
        n = len(events)
        def bi_search(nums, tar):
            low, high = 0, n - 1
            while low < high:
                mid = (low + high) // 2
                if nums[mid] < tar:
                    low = mid + 1
                else:
                    high = mid
            return low
        
        events.sort(key=lambda x: x[1])
        ends = [e for _, e, _ in events]

        ans = 0
        max_seconds = {}
        best = 0
        for idx, val in enumerate(events):
            best = max(best, val[-1])
            max_seconds[idx] = max(val[-1], best)
        
        for i in range(n-1, -1, -1):
            ans = max(ans, events[i][-1])
            idx = bi_search(ends, events[i][0]) - 1
            if idx >= 0:
                ans = max(ans, events[i][-1] + max_seconds[idx]) # 最近最小的
            
        return ans


    def maxTwoEvents(self, events: List[List[int]]) -> int:
        return self.sort_bi_search(events)
        

if __name__ == '__main__':
    events = [[1,3,2],[4,5,2],[2,4,3]] # 4
    # events =[[1,3,2],[4,5,2],[1,5,5]] # 5
    events = [[1,5,3],[1,5,1],[6,6,5]] # 8
    events = [[66,97,90],[98,98,68],[38,49,63],[91,100,42],[92,100,22],[1,77,50],[64,72,97]]
    # events = [[35,90,47],[72,80,70]]


    s = Solution()
    print(s.maxTwoEvents(events))

# @lc code=end

