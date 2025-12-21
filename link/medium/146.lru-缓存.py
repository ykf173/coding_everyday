#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start
class LinkNode:
    def __init__(self, key: int=-1, val:int=-1, pre=None, post=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.post = post

class LRUCache:
    '''映射表+双向链表'''
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_dict = {} # key: node
        self.cur_cap = 0
        self.head = LinkNode(val=-1)
        self.tail = LinkNode(val=-1)
        self.head.post = self.tail # value: node
        self.tail.pre = self.head

    def del_node(self, node):
        node.pre.post = node.post
        node.post.pre = node.pre
        # return node


    def insert_node(self, p):
        p.post = self.head.post
        self.head.post.pre = p
        p.pre = self.head
        self.head.post = p

    def print_nodes(self):
        print(self.head.val, end=' -> ')

        p = self.head.post
        while p and p.post:
            print(p.val, end=' -> ')
            p = p.post
        print(self.tail.val)

    def get(self, key: int) -> int:
        res = self.lru_dict.get(key, -1)
        # if res!=-1:
        #     print(res.val)
        if res != -1:
            self.del_node(res)
            self.insert_node(res)
        else:
            return res
    
        return res.val
        

    def put(self, key: int, value: int) -> None:
        res = self.lru_dict.get(key, -1)
        # print('put')
        if res == -1: # 没找到
            node = LinkNode(key=key, val=value)
            if self.cur_cap < self.capacity:
                self.insert_node(node)
                self.lru_dict[key] = node
                self.cur_cap += 1
            else:
                if self.tail.pre != self.head:
                    # self.print_nodes()
                    self.lru_dict.pop(self.tail.pre.key)
                    self.del_node(self.tail.pre)
                self.insert_node(node)
                self.lru_dict[key] = node
        else:
            self.del_node(res)
            self.insert_node(res)
            self.lru_dict[key].val = value


# ["LRUCache","put","put"]\n[[2],[1,1],[2,2]]
# ["LRUCache","put","put", "get", "get"]\n[[2],[1,1],[2,2],[2],[1]]
# ["LRUCache","put","put", "get", "put"]\n[[2],[1,1],[2,2],[2],[3,3]]
# ["LRUCache","put","put", "get", "put", "get","put"]\n[[2],[1,1],[2,2],[2],[3,3],[4], [1,4]]
# ["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
# ["LRUCache","put","put","get","put","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2]]
# ["LRUCache","put","put","get","put"]\n[[2],[1,1],[2,2],[1],[3,3]]
# ["LRUCache","put","put","get","put","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2]]
# ["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,0],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

