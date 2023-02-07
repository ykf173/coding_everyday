# 
# 
# 给你一棵 完整二叉树的根，这棵树有以下特征：
# 
# 叶子节点要么值为0要么值为1，其中0 表示False，1 表示True。
# 非叶子节点 要么值为 2要么值为 3，其中2表示逻辑或OR ，3表示逻辑与AND。
# 计算一个节点的值方式如下：
# 
# 如果节点是个叶子节点，那么节点的 值为它本身，即True或者False。
# 否则，计算两个孩子的节点值，然后将该节点的运算符对两个孩子值进行 运算。
# 返回根节点root的布尔运算值。
# 
# 完整二叉树是每个节点有 0个或者 2个孩子的二叉树。
# 
# 叶子节点是没有孩子的节点。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：root = [2,1,3,None,None,0,1]
# 输出：true
# 解释：上图展示了计算过程。
# AND 与运算节点的值为 False AND True = False 。
# OR 运算节点的值为 True OR False = True 。
# 根节点的值为 True ，所以我们返回 true 。
# 示例 2：
# 
# 输入：root = [0]
# 输出：false
# 解释：根节点是叶子节点，且值为 false，所以我们返回 false 。
# 
# 
# 提示：
# 
# 树中节点数目在[1, 1000]之间。
# 0 <= Node.val <= 3
# 每个节点的孩子数为0 或2。
# 叶子节点的值为0或1。
# 非叶子节点的值为2或3 。
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createTree(self, L: list):
        root = TreeNode(L[0])
        p = root
        lenL = len(L)
        for i in range(1, lenL):
            s = TreeNode(L[i])

            if i % 2 != 0 and L[i] != None:
                p.left = s

            elif i % 2 == 0 and L[i] != None:
                p.right = s
                p = s

        return root

    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left:
            return root.val == 1
        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)

        return self.evaluateTree(root.left) and self.evaluateTree(root.right)


if __name__ == '__main__':
    L = [2, 1, 3, None, None, 0, 1]
    # L = [0]
    L = [3, 2, 3, 2, 2, 3, 2, 1, 1, 2, 3, 0, 1, 0, 3, None, None, None, None, 0, 2, 3, 2, None, None, None, None, None,
         None, 0, 0, None, None, 1, 1, 0, 0, 1, 3, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, 3, 0, 1, 1, None, None, None, None, None, None]
    s = Solution()
    root = s.createTree(L)
    t = s.evaluateTree(root)
    print(t)
