#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
from collections import deque
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bfs(self, root):
        if not root:
            return []
        
        ans = []
        lay_nodes = deque([root])
        while lay_nodes:
            nums = len(lay_nodes)
            cur_lay = []
            for i in range(nums):
                p = lay_nodes.popleft()
                left, right = p.left, p.right
                if left:
                    lay_nodes.append(left)
                if right:
                    lay_nodes.append(right)
                cur_lay.append(p.val)
            if cur_lay:
                ans.append(cur_lay)
        return ans


    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.bfs(root)

# if __name__ == '__main__':

# @lc code=end

