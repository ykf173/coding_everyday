#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
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
    def __init__(self):
        self.res = []


    def create_tree(self, nums: List[int]):
        root = TreeNode(nums[0])
        seq = deque([root])
        n = len(nums)
        i = 1
        p = root
        while seq and i < n:
            p = seq.popleft()

            if p and nums[i] is not None:
                node = TreeNode(nums[i])
                p.left = node
                seq.append(p.left)
            if i + 1 < n and p and nums[i+1] is not None:
                node = TreeNode(nums[i+1])
                p.right = node
                seq.append(p.right)
            i += 2
        return root
    
    def preorderTraversal_v0(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        p = root
        res = []
        while p or stack:
            if p:
                res.append(p.val)
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                p = p.right

        return res
            

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if root:
        #     self.res.append(root.val)
        #     self.preorderTraversal(root.left)
        #     self.preorderTraversal(root.right)
        
        # return self.res
        return self.preorderTraversal_v0(root)
    

# @lc code=end
if __name__ == "__main__":
    s = Solution()
    nums = [1, None, 2, 3]
    nums = [1, 2, 3, None, 5, 6, None, 7, 8]

    root = s.create_tree(nums)
    print('原始:', nums)

    print('非递归：', s.preorderTraversal_v0(root))

    print('递归：', s.preorderTraversal(root))




