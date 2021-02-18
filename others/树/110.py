# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BiTree:
    def __init__(self, root=None):
        self.root = root

    def preOrder(self, node):
        if node:
            print(node.val, end=';')
        if node.left:
            self.preOrder(node.left)
        if node.right:
            self.preOrder(node.right)

    def addNode(self, value):
        node = TreeNode(value)
        if not self.root:
            self.root = node
        else:
            queque = [self.root]
            while queque:
                point = queque.pop(0)
                if not point.left:
                    point.left = node
                    return
                else:
                    queque.append(point.left)

                if not point.right:
                    point.right = node
                    return
                else:
                    queque.append(point.right)

    def createTree(self, node, values, index):
        if index < len(values):
            if not values[index]:
                return None
            node = TreeNode(values[index])
            node.left = self.createTree(node.left, values, 2 * index + 1)
            node.right = self.createTree(node.right, values, 2 * index + 2)

            return node
        return node


class Solution:
    def depth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return max(self.depth(root.left), self.depth(root.right)) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.depth(root.left) - self.depth(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(
            root.right)


if __name__ == '__main__':
    s = Solution()

    # while 1:
    l0 = [3, 9, 20, None, None, 15, 7]
    l1 = [1, 2, 2, 3, 3, None, None, 4, 4]
    # root = TreeNode(None)
    # print(s.isBalanced(root))
    for i in range(2):
        l = eval(f'l{i}')
        tree = BiTree()
        tree.root = tree.createTree(tree.root, l, 0)
        # for val in l[1:]:
        #     tree.addNode(val)
        # tree.preOrder(tree.root)

        print(s.isBalanced(tree.root))

'''
3,9,20,null,null,15,7
1,2,2,3,3,null,null,4,4

'''
