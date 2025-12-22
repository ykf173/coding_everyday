class BiTree:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def read_tree2(root):
    res = []
    if not root:
        return res
        
    cur = [root]
    if root.val:
        res = [root.val]

    p = root
    while p and cur:
        res.append([root.val])
        if p.left:
            res.append(p[0].left.val)
            cur.append(p[0].left)
        if p.right:
            res.append(p[0].right.val)
            cur.append(p[0].right)

        p = cur.pop(0)

        

def read_tree(root):

    if root:
        return [root.val]
    return read_tree(root.left) + read_tree(root.right)
