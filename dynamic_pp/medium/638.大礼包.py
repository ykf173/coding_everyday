#
# @lc app=leetcode.cn id=638 lang=python3
#
# [638] 大礼包
#

# @lc code=start
from functools import lru_cache
from typing import List, Tuple
class Solution:
    def __init__(self):
        self.price = []
        self.special = []

    @lru_cache(maxsize=128)
    def dfs(self, need_tuple: Tuple[int]) -> int:
        m = len(need_tuple)

        min_price = sum(need_tuple[i] * self.price[i] for i in range(m))

        for sp in self.special:
            need_list = list(need_tuple)
            is_use = True
            for i in range(m):
                if sp[i] > need_list[i]:
                    is_use = False
                    break
                need_list[i] -= sp[i]

            if is_use:
                min_price = min(min_price, self.dfs(tuple(need_list)) + sp[-1])
                
        return min_price

    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        m = len(needs)

        total_price = sum(needs[i] * price[i] for i in range(m))
        filter_p = []
        for sp in special:
            if sum(sp[-1] for sp in special) >= 0 and sum(needs[i] * price[i] for i in range(m)) > sp[-1]: # 坑货大礼包
                filter_p.append(sp)
        
        filter_p = [sp for sp in filter_p if 0 <= sp[-1] <= total_price and all([needs[i] >= sp[i] for i in range(m)])] # 无效大礼包

        self.price = price
        self.special = filter_p

        return self.dfs(tuple(needs))
    
if __name__ == '__main__':
    price = [2,5]; special = [[3,0,5],[1,2,10]]; needs = [3,2]
    # price = [2,3,4]; special = [[1,1,0,4],[2,2,1,9]]; needs = [1,2,1]
    price = [1,1,1]; special = [[1,1,0,0],[2,2,1,9]]; needs = [1,1,0]

    price = [1,1,1]; special = [[1,1,0,0],[2,2,1,0]]; needs = [1,1,1]
    s = Solution()
    print(s.shoppingOffers(price, special, needs))
        
# @lc code=end

