#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
from typing import List
from collections import defaultdict

class Solution:
    def sort_dict(self, s: str, p: str) -> List[int]:
        dic = defaultdict(list)
        n, k = len(s), len(p)

        if k > n:
            return []
        for i in range(n-k+1):
            dic[''.join(sorted(list(s[i:i+k])))].append(i)
        
        p = ''.join(list(sorted(p)))
        res = list(dic[p]) if p in dic else []
        return res
    
    def move_window(self, s: str, p: str) -> List[int]:
        res = []
        m, n = len(s), len(p)
        s_cnt, p_cnt = [0] * 26, [0] * 26
        if m < n:
            return []
        
        for i in range(n): # n < m，为了一起算，这里也统计了s_cnt
            s_cnt[ord(s[i]) - 97] += 1
            p_cnt[ord(p[i]) - 97] += 1

        if s_cnt == p_cnt:
            res.append(0)
        
        for i in range(m-n): # 滑动窗口
            s_cnt[ord(s[i]) - 97] -= 1
            s_cnt[ord(s[i+n]) - 97] += 1

            if s_cnt == p_cnt:
                res.append(i+1)

        return res


    def findAnagrams(self, s: str, p: str) -> List[int]:
        # return self.sort_dict(s, p)
        return self.move_window(s, p)
    

if __name__ == '__main__':
    import time

    s = Solution()
    st, p = "cbaebabacd",  "abc"
    # st, p = "abab", "ab"
    # st, p = "abab", "b"
    # st, p = "abab", "ababc"
    
    print(s.sort_dict(st, p))
    print(s.findAnagrams(st, p))
# @lc code=end

