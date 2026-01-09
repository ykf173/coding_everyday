#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
from typing import List, Optional
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        def build(l, r): # dfs
            res = []
            if l > r:
                return [None]
            if (l, r) in memo:
                return memo[(l, r)]
            
            for i in range(l, r+1):
                lefts = build(l, i-1)
                rights = build(i+1, r)
                for left in lefts:
                    for right in rights:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        res.append(root)
            memo[(l, r)] = res
            return res
        return build(1, n)
# @lc code=end

