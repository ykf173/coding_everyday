#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def recurative_method(self, root):
        if not root:
            return []
        if root:
            self.recurative_method(root.left)
            self.recurative_method(root.right)
            self.ans.append(root.val)
        
    def iterative_method1(self, root):
        stack = []

        p = root
        while root or p:
            if p:
                stack.append(p.left)
                stack.append(p.right)
                p = p.right
            else:
                p = stack.pop()
                self.ans.append(p.val)

            
    def iterative_method2(self, root):
        stack = [root]
        # stack_right = []

        while stack:
            p = stack.pop()
            self.ans.append(p.val)
            if p.left:
                stack.append(p.left)
            if p.right:
                stack.append(p.right)
        
        # return self.ans[::-1]


    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        # self.recurative_method(root)
        self.iterative_method2(root)

        return self.ans[::-1]

# [1,2,3,4,5,null,8,null,null,6,7,9]
#  [1,2,3,null,5,6,null,7,8] 
# @lc code=end

