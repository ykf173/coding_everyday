from typing import List


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:  # 超时
        operater_num = 0
        len_s = len(s)
        i = 0

        while i < len_s:
            ch = s[i]
            max_num = total = 0
            while i < len_s and ch == s[i]:
                max_num = max(max_num, cost[i])
                total += cost[i]
                i += 1
            operater_num += total - max_num

        return operater_num


if __name__ == '__main__':
    s = Solution()

    s0, cost0 = "aaabbbabbbb", [3, 5, 10, 7, 5, 3, 5, 5, 4, 8, 1]
    s1, cost1 = "abc", [1, 2, 3]
    s2, cost2 = "abaac", [1, 2, 3, 4, 5]
    s3, cost3 = "aaabaac", [2, 1, 3, 3, 4, 5, 6]
    s4, cost4 = "aabaa", [1, 2, 3, 4, 1]
    s5, cost5 = "aaaaaaa", [3, 2, 1, 4, 5, 6, 3]

    for i in range(6):
        ss = eval('s%s' % i)
        cost = eval('cost%s' % i)

        print(s.minCost(ss, cost))
