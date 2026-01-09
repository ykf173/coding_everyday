#
# @lc app=leetcode.cn id=1339 lang=python3
#
# [1339] 分裂二叉树的最大乘积
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional
class Solution:
    def __init__(self):
        self.memo = {}

    def dfs(self, root: Optional[TreeNode]) -> int:
        total = 0
        if not root:
            return total
        if root in self.memo:
            return self.memo[root]

        total = root.val + self.dfs(root.left) + self.dfs(root.right)
        self.memo[root] = total
        return total
    
    def bfs_dfs(self, root: Optional[TreeNode]) -> int:
        max_val = 10 ** 9 + 7 
        ans = 0
        squence = deque([root])

        total = self.dfs(root)
        self.memo[root] = total
        while squence:
            node = squence.popleft()
            t1, t2 = 0, 0
            if node.left:
                squence.append(node.left)
                t1 = self.memo.get(node.left)
                ans = max(ans, (total - t1) * t1)
            if node.right:
                squence.append(node.right)
                t2 = self.memo.get(node.right)
                ans = max(ans, (total - t2) * t2)
        return ans % max_val
    
    def test(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        subs = []

        def sum_tree(node):
            if not node:
                return 0
            s = node.val + sum_tree(node.left) + sum_tree(node.right)
            subs.append(s)
            return s

        total = sum_tree(root)
        best = 0
        for s in subs:
            best = max(best, s * (total - s))
        return best % MOD

    def memo_dfs(self, root: Optional[TreeNode]) -> int:
        max_val = 10**9 + 7
        ans = 0
        memo = []

        def dfs(node):
            if not node:
                return 0
            total = node.val + dfs(node.left) + dfs(node.right)
            memo.append(total)
            return total
        
        total = dfs(root)
        for t in memo:
            ans = max(ans, (total - t) * t)

        return ans % max_val

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # return self.bfs_dfs(root)
        return self.memo_dfs(root)
        # return self.test(root)
    
    

# @lc code=end

