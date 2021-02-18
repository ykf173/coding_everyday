from typing import List, Dict
from collections import defaultdict

"""
1. 该题用通用解法比较困难，顺序判断解决不了acounts3类型为问题
2. 涉及到连通图图论问，应该使用并查集。
"""
class Solution:
    def sort_accounts(self, accounts):
        for index, account in enumerate(accounts):
            accounts.pop(index)
            accounts.insert(index, [account[0]] + sorted(account[1:]))

        return accounts

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        account_list = []
        names = []
        for account in accounts:
            if account[0] not in names:
                names.append(account[0])
                account_list.append([account[0]] + list(set(account[1:])))
            else:
                for index, acco in enumerate(account_list):
                    inter = set(account[1:]).intersection(set(acco[1:]))
                    if acco[0] == account[0] and inter:
                        account_list.pop(index)
                        new_mails = [account[0]] + list(set(account[1:] + acco[1:]))
                        account_list.insert(index, new_mails)
                        break

                else:
                    account_list.append([account[0]] + list(set(account[1:])))

        accounts = self.sort_accounts(account_list)
        return accounts


s = Solution()
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"],
            ["John", "johnbmith@mail.com", "john_aewyork@mail.com", "john00@mail.com"]]

accounts2 = [["Alex", "Alex5@m.co", "Alex4@m.co", "Alex0@m.co"], ["Ethan", "Ethan3@m.co", "Ethan3@m.co", "Ethan0@m.co"],
             ["Kevin", "Kevin4@m.co", "Kevin2@m.co", "Kevin2@m.co"], ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe2@m.co"],
             ["Gabe", "Gabe3@m.co", "Gabe4@m.co", "Gabe2@m.co"]]

accounts3 = [["David", "David0@m.co", "David1@m.co"], ["David", "David3@m.co", "David4@m.co"],
             ["David", "David4@m.co", "David5@m.co"], ["David", "David2@m.co", "David3@m.co"],
             ["David", "David1@m.co", "David2@m.co"]]

accs = s.accountsMerge(accounts3)
for acc in accs:
    print(acc)

s = [["Alex", "Alex0@m.co", "Alex4@m.co", "Alex5@m.co"], ["Ethan", "Ethan0@m.co", "Ethan3@m.co"],
     ["Gabe", "Gabe0@m.co", "Gabe2@m.co", "Gabe3@m.co", "Gabe4@m.co"], ["Kevin", "Kevin2@m.co", "Kevin4@m.co"]]

s3 = [["David", "David0@m.co", "David1@m.co", "David2@m.co"],
      ["David", "David2@m.co", "David3@m.co", "David4@m.co", "David5@m.co"]]

s4 = [["David", "David0@m.co", "David1@m.co", "David2@m.co", "David3@m.co", "David4@m.co", "David5@m.co"]]
