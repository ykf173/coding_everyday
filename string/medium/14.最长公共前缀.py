#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
from typing import List

class Solution:
    def baolilongestCommonPrefix(self, strs: List[str]) -> str:
        min_str = strs[0]
        for st in strs:
            if len(st) < len(min_str):
                min_str = st

        ans = ''
        strs = [st for st in strs if st != min_str]
        n = len(strs)
        for i in range(len(min_str)):
            for j in range(n):
                if strs[j][i] != min_str[i]:
                    return ans
            ans += min_str[i]
        return ans


    def map_method(self, strs: List[str]) -> str:
        dict = {}
        # if len(strs) == 0:
        #     return ''
        # if len(strs) == 1:
        #     return strs[0]
        # min_str, max_str = strs[0], strs[1]
        min_str = max_str = strs[0]
        ans = ''
        if not min_str or not max_str:
            return ''
        for st in strs:
            if st < min_str:
                min_str = st
            if st > max_str:
                max_str = st
        
        for i in range(len(min_str)):
            dict[i] = min_str[i]

        for i in range(len(max_str)):
            if i in dict and dict[i] == max_str[i]:
                ans += min_str[i]
            else:
                break
        return ans
            
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
       return self.map_method(strs)
        
# @lc code=end

if __name__ == '__main__':

    strs = ["flower","flow","flight"]
    strs = ["dog","racecar","car"]
    strs = ["ab", "a"]
    s = Solution()
    print(strs, s.longestCommonPrefix(strs))