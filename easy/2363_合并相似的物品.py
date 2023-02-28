# 给你两个二维整数数组 items1 和 items2 ，表示两个物品集合。每个数组 items 有以下特质：
# 
# items[i] = [valuei, weighti] 其中 valuei 表示第 i 件物品的 价值 ，weighti 表示第 i 件物品的 重量 。
# items 中每件物品的价值都是 唯一的 。
# 请你返回一个二维数组 ret，其中 ret[i] = [valuei, weighti]， weighti 是所有价值为 valuei 物品的 重量之和 。
# 
# 注意：ret 应该按价值 升序 排序后返回。
# 
#  
# 
# 示例 1：
# 
# 输入：items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]
# 输出：[[1,6],[3,9],[4,5]]
# 解释：
# value = 1 的物品在 items1 中 weight = 1 ，在 items2 中 weight = 5 ，总重量为 1 + 5 = 6 。
# value = 3 的物品再 items1 中 weight = 8 ，在 items2 中 weight = 1 ，总重量为 8 + 1 = 9 。
# value = 4 的物品在 items1 中 weight = 5 ，总重量为 5 。
# 所以，我们返回 [[1,6],[3,9],[4,5]] 。
# 示例 2：
# 
# 输入：items1 = [[1,1],[3,2],[2,3]], items2 = [[2,1],[3,2],[1,3]]
# 输出：[[1,4],[2,4],[3,4]]
# 解释：
# value = 1 的物品在 items1 中 weight = 1 ，在 items2 中 weight = 3 ，总重量为 1 + 3 = 4 。
# value = 2 的物品在 items1 中 weight = 3 ，在 items2 中 weight = 1 ，总重量为 3 + 1 = 4 。
# value = 3 的物品在 items1 中 weight = 2 ，在 items2 中 weight = 2 ，总重量为 2 + 2 = 4 。
# 所以，我们返回 [[1,4],[2,4],[3,4]] 。
# 示例 3：
# 
# 输入：items1 = [[1,3],[2,2]], items2 = [[7,1],[2,2],[1,4]]
# 输出：[[1,7],[2,4],[7,1]]
# 解释：
# value = 1 的物品在 items1 中 weight = 3 ，在 items2 中 weight = 4 ，总重量为 3 + 4 = 7 。
# value = 2 的物品在 items1 中 weight = 2 ，在 items2 中 weight = 2 ，总重量为 2 + 2 = 4 。
# value = 7 的物品在 items2 中 weight = 1 ，总重量为 1 。
# 所以，我们返回 [[1,7],[2,4],[7,1]] 。
#  
# 
# 提示：
# 
# 1 <= items1.length, items2.length <= 1000
# items1[i].length == items2[i].length == 2
# 1 <= valuei, weighti <= 1000
# items1 中每个 valuei 都是 唯一的 。
# items2 中每个 valuei 都是 唯一的 。
from collections import defaultdict
from typing import List


class Solution:
    def mergeSimilarItems1(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items1 += items2
        items1.sort()
        len_items = len(items1)
        items = [items1[0]]
        for i in range(1, len_items):
            if items1[i][0] == items1[i - 1][0]:
                if items[-1][0] == items1[i][0]:
                    items[-1][1] += items1[i][1]
                else:
                    items.append([items1[i][0], items1[i][1] + items1[i - 1][1]])
            else:
                items.append(items1[i])
        return items

    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        its = defaultdict(int)

        for k, v in items1:
            its[k] += v

        for k, v in items2:
            its[k] += v
        res = sorted(its.items(), key=lambda x: x[0])
        res = [[a, b] for a, b in res]
        return res


if __name__ == '__main__':
    iterm1s = [
        # [[1, 1], [4, 5], [3, 8]],
        # [[1, 1], [3, 2], [2, 3]],
        # [[1, 3], [2, 2]],
        [[5, 1], [4, 2], [3, 3], [2, 4], [1, 5]]
    ]

    iterm2s = [
        # [[3, 1], [1, 5]],
        # [[2, 1], [3, 2], [1, 3]],
        # [[7, 1], [2, 2], [1, 4]],
        [[7, 1], [6, 2], [5, 3], [4, 4]]

    ]
    # [[1,5],[2,4],[3,3],[4,6],[5,4],[6,2],[7,1]]
    s = Solution()

    for iterm1, iterm2 in zip(iterm1s, iterm2s):
        print(s.mergeSimilarItems(iterm1, iterm2))
