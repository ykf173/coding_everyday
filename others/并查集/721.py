from collections import defaultdict
from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def union(self, index1: int, index2: int):
        self.parent[self.find(index2)] = self.find(index1)

    def find(self, index: int) -> int:
        if self.parent[index] != index:
            self.parent[index] = self.find(self.parent[index])
        return self.parent[index]


class Solution:
    def __init__(self):
        self.email2index = {}
        self.email2name = {}

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        for account in accounts:  # 初始化哈希表
            name = account[0]
            for email in account[1:]:
                if email not in self.email2index:
                    self.email2index[email] = len(self.email2index)
                    self.email2name[email] = name

        uf = UnionFind(len(self.email2index))  # 初始化并查集

        for account in accounts:  # 合并连通图
            firstIndex = self.email2index[account[1]]
            for email in account[2:]:
                uf.union(firstIndex, self.email2index[email])

        index2Emails = defaultdict(list)  # 建立哈希表反查并查集，index对应的emails
        for email, index in self.email2index.items():
            index = uf.find(index)
            index2Emails[index].append(email)

        ans = []
        for emails in index2Emails.values(): # 输出对应答案并排序，这里的emails中对应的人都是同一个人，可以利用哈希表反查回去
            ans.append([self.email2name[emails[0]]] + sorted(emails))
        return ans


if __name__ == '__main__':
    s = Solution()
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"],
                ["John", "johnbmith@mail.com", "john_aewyork@mail.com", "john00@mail.com"]]

    accounts2 = [["Alex", "Alex5@m.co", "Alex4@m.co", "Alex0@m.co"],
                 ["Ethan", "Ethan3@m.co", "Ethan3@m.co", "Ethan0@m.co"],
                 ["Kevin", "Kevin4@m.co", "Kevin2@m.co", "Kevin2@m.co"],
                 ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe2@m.co"],
                 ["Gabe", "Gabe3@m.co", "Gabe4@m.co", "Gabe2@m.co"]]

    accounts3 = [["David", "David0@m.co", "David1@m.co"], ["David", "David3@m.co", "David4@m.co"],
                 ["David", "David4@m.co", "David5@m.co"], ["David", "David2@m.co", "David3@m.co"],
                 ["David", "David1@m.co", "David2@m.co"]]

    accs = s.accountsMerge(accounts)
    for acc in accs:
        print(acc)
