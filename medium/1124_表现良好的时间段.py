# 给你一份工作时间表hours，上面记录着某一位员工每天的工作小时数。
# 
# 我们认为当员工一天中的工作小时数大于8 小时的时候，那么这一天就是「劳累的一天」。
# 
# 所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。
# 
# 请你返回「表现良好时间段」的最大长度。
# 
# 
# 
# 示例 1：
# 
# 输入：hours = [9,9,6,0,6,6,9]
# 输出：3
# 解释：最长的表现良好时间段是 [9,9,6]。
# 示例 2：
# 
# 输入：hours = [6,6,6]
# 输出：0
# 
# 
# 提示：
# 
# 1 <= hours.length <= 104
# 0 <= hours[i] <= 16
from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        len_L = len(hours)
        i = 0
        j = 0
        tired_days = 0
        max_len = 0
        while i < len_L:
            while j < len_L:
                if hours[j] > 8:
                    j += 1
                    tired_days += 1
                if hours[i] <= 8 and tired_days <= j - i + 1 - tired_days:
                    i += 1
                if hours[i] > 8:  # tired_days > j - i + 1 - tired_days
                    max_len = max(j - i + 1, tired_days)
                i += 1
                j += 1

        return max_len


if __name__ == '__main__':
    s = Solution()
    inputs = [
        [6, 6, 6],
        [9, 9, 6, 0, 6, 6, 9],
        [0, 0, 0, 0]
    ]

    for hours in inputs:
        print(s.longestWPI(hours))
