from collections import defaultdict
from typing import List

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        allow_dic = defaultdict(list)
        for x in allowed:
            allow_dic[(x[0], x[1])].append(x[2])

        memo = {}
        def solve(row):
            if len(row) == 1:
                return True
            if row in memo:
                return memo[row]

            for i in range(len(row) - 1):
                if (row[i], row[i+1]) not in allow_dic:
                    memo[row] = False
                    return False

            def create_next_layer(pos, path_list): # dfs，不用字符串因为字符串是静态的，不能改
                if pos == len(row) - 1: # 到顶了
                    return solve(''.join(path_list))

                a, b = row[pos], row[pos+1]
                for c in allow_dic[(a, b)]:
                    path_list.append(c)
                    if create_next_layer(pos+1, path_list):
                        return True
                    path_list.pop()
                return False

            ans = create_next_layer(0, [])
            memo[row] = ans
            return ans
        
        return solve(bottom)
    
if __name__ == '__main__':
    bottom = "AAAA"
    allowed = ["AAB","AAC","BCD","BBE","DEF"]
    s = Solution()
    print(s.pyramidTransition(bottom, allowed))