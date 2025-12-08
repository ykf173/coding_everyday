#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
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
    def bfs(self, root):
        if not root:
            return []
        ans = []
        layer_nodes = deque([root])
        while layer_nodes:
            cur_layer = []
            n = len(layer_nodes)
            for _ in range(n):
                p = layer_nodes.popleft()
                left, right = p.left, p.right

                if left:
                    layer_nodes.append(left)
                if right:
                    layer_nodes.append(right)
                cur_layer.append(p.val)
            if cur_layer:
                ans.append(cur_layer)
        return ans

    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = self.bfs(root)
        return ans[::-1]
# @lc code=end

