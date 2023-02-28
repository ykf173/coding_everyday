# 一所学校里有一些班级，每个班级里有一些学生，现在每个班都会进行一场期末考试。给你一个二维数组 classes，其中classes[i] = [passi, totali]，表示你提前知道了第i个班级总共有totali个学生，其中只有passi个学生可以通过考试。
# 
# 给你一个整数extraStudents，表示额外有extraStudents个聪明的学生，他们 一定能通过任何班级的期末考。你需要给这extraStudents个学生每人都安排一个班级，使得 所有班级的 平均通过率 最大。
# 
# 一个班级的通过率等于这个班级通过考试的学生人数除以这个班级的总人数。平均通过率是所有班级的通过率之和除以班级数目。
# 
# 请你返回在安排这 extraStudents 个学生去对应班级后的 最大平均通过率。与标准答案误差范围在10-5以内的结果都会视为正确结果。
# 
# 
# 
# 示例 1：
# 
# 输入：classes = [[1,2],[3,5],[2,2]], extraStudents = 2
# 输出：0.78333
# 解释：你可以将额外的两个学生都安排到第一个班级，平均通过率为 (3/4 + 3/5 + 2/2) / 3 = 0.78333 。
# 示例 2：
# 
# 输入：classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
# 输出：0.53485
# 
# 
# 提示：
# 
# 1 <= classes.length <= 105
# classes[i].length == 2
# 1 <= passi <= totali <= 105
# 1 <= extraStudents <= 105

import heapq  # 小根堆
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        diff = lambda x, y: (x + 1) / (y + 1) - x / y
        ans = 0.
        que = []
        for x, y in classes:
            que.append((-diff(x, y), x, y))
            ans += x / y

        heapq.heapify(que)

        for _ in range(extraStudents):
            di, x, y = heapq.heappop(que)
            ans -= di
            heapq.heappush(que, (-diff(x + 1, y + 1), x + 1, y + 1))
        return ans / len(que)


# class Solution:
#     def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
#         diff = lambda x, y: (x + 1) / (y + 1) - x / y
#
#         q = list()
#         ans = 0.
#         for x, y in classes:
#             ans += x / y
#             # python 中的优先队列是小根堆，所以要对增加量取相反数，达到大根堆的效果
#             q.append((-diff(x, y), x, y))
#
#         heapq.heapify(q)  # 建大根堆
#
#         for _ in range(extraStudents):
#             d, x, y = heapq.heappop(q)  # 取出最大的，繼續加一
#             ans += -d
#             heapq.heappush(q, (-diff(x + 1, y + 1), x + 1, y + 1))
#
#         return ans / len(classes)


if __name__ == '__main__':
    s = Solution()
    classes = [[1, 2], [3, 5], [2, 2]]
    classes = [[2, 4], [3, 9], [4, 5], [2, 10]]
    extraStudents = 2
    extraStudents = 4
    print(s.maxAverageRatio(classes, extraStudents))
