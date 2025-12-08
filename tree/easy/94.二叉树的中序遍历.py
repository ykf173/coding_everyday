#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional, List

class Solution:
    def __init__(self):
        self.ans = []

    def recursive_method(self, root):
        if root:
            self.recursive_method(root.left)
            self.ans.append(root.val)
            self.recursive_method(root.right)
        return self.ans

    
    def iterative_method(self, root): # 非递归
        if not root:
            return []
        ans = []
        stack = []
        p = root
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                ans.append(p.val)
                p = p.right
        return ans


    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # self.recursive_method(root)
        
        # return self.ans
        return self.iterative_method(root)


# [1,2,3,null,5,6,null,7,8]
# @lc code=end

