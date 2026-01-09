#
# @lc app=leetcode.cn id=2402 lang=python3
#
# [2402] 会议室 III
#

# @lc code=start
from typing import List
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        available = list(range(n))          # 空闲房间：按房间号小根堆
        heapq.heapify(available)
        
        busy = []                           # 占用房间：(结束时间, 房间号) 小根堆
        cnt = [0] * n
        
        for s, e in meetings:
            dur = e - s
            
            # 释放已经结束的房间
            while busy and busy[0][0] <= s:
                end_time, rid = heapq.heappop(busy)
                heapq.heappush(available, rid)
            
            if available:
                rid = heapq.heappop(available)
                heapq.heappush(busy, (e, rid))
                cnt[rid] += 1
            else:
                end_time, rid = heapq.heappop(busy)
                # 顺延：从 end_time 开始
                heapq.heappush(busy, (end_time + dur, rid))
                cnt[rid] += 1
        
        # 找使用次数最多的房间，次数相同取最小编号
        best = 0
        for i in range(1, n):
            if cnt[i] > cnt[best]:
                best = i
        return best


if __name__ == '__main__':
    n = 2; meetings = [[0,10],[1,5],[2,7],[3,4]]
    n = 3; meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
    s = Solution()
    print(s.mostBooked(n, meetings))
# @lc code=end

