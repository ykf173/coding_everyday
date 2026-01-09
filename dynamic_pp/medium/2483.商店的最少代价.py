#
# @lc app=leetcode.cn id=2483 lang=python3
#
# [2483] 商店的最少代价
#

# @lc code=start
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)

        min_cnt = cnt = sum(1 for i in range(n) if customers[i] == 'Y')
        ans = 0
        for i in range(n):
            if customers[i] == 'N': # 开门，没人
                cnt += 1
            else:
                cnt -= 1
            if cnt < min_cnt:
                min_cnt = cnt
                ans = i + 1

        return ans

if __name__ == '__main__':
    # s = 'YYNY'
    s = 'YNNY'
    ss = Solution()
    print(ss.bestClosingTime(s))

# @lc code=end

