'''
给定两个节点，找其最早祖先
'''


class biTreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_bi_tree(li):
    if not li:
        return None
    val = li.pop(0)
    if not val:
        return None

    root = biTreeNode(val)
    root.left = create_bi_tree(li)
    root.right = create_bi_tree(li)
    return root


def get_path(root, target, path=[]):
    if not root:
        return

    if root.val == target:
        return path

    path.append(root.val)

    left_path = get_path(root.left, target, path)
    if left_path:
        return path

    right_path = get_path(root.right, target, path)
    if right_path:
        return path

    path.pop()
    return []


def get_fa(root):
    path1 = get_path(root, 4, [])

    path2 = get_path(root, 10, [])

    print(path1, path2)
    while path1:
        top = path1.pop()
        if top in path2:
            return top
    return None



if __name__ == '__main__':
    li = [1, 2, None, None, 3, 4, None, None, 5, 8, 9, None, 10]
    path = []
    root = create_bi_tree(li)
    print(get_fa(root))