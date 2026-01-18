#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        cur_seq, next_seq = deque([root]), deque()

        ans = [root.val]
        p = root
        cur_sum, cur_len = 0, 0
        while cur_seq:
            # print(len(cur_seq), len(next_seq))
            p = cur_seq.popleft()

            # if not cur_seq:
            #     # cur_seq = next_seq
            #     # next_seq = deque()
            #     ans.append(round(cur_sum / cur_len, 5) if cur_len else 0)
            #     # print(p.val, cur_sum, cur_len, ans)
            #     cur_sum, cur_len = 0, 0

            if p.left:
                next_seq.append(p.left)
                cur_sum += p.left.val
                cur_len += 1

            if p.right:
                next_seq.append(p.right)
                cur_sum += p.right.val
                cur_len += 1

            # print(p.val, cur_sum, cur_len, ans)
            
            if not cur_seq and next_seq:
                ans.append(round(cur_sum / cur_len, 5) if cur_len else 0)
                cur_sum, cur_len = 0, 0
                cur_seq = next_seq
                next_seq = deque()
        return ans
        
# [3,9,20,null,null,15,7] 
# [3,9,20,15,7]
# @lc code=end

