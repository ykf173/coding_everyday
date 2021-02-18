from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        if rowIndex == 0:
            return ans

        else:
            lastRow = self.getRow(rowIndex - 1)
            for i in range(rowIndex - 1):
                ans.append(lastRow[i] + lastRow[i + 1])

        ans.append(1)
        return ans


if __name__ == '__main__':
    s = Solution()
    while 1:
        rowIndex = int(input())
        print(s.getRow(rowIndex))

'''

'''
