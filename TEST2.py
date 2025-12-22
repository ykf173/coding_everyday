from typing import List


class Solution:
    def sort_list(self, time_list: List[List[int]]):
        if len(time_list) <= 1:
            return time_list
        return self.sort_list([t for t in time_list if t < time_list[0]]) + [time_list[0]] + self.sort_list([t for t in time_list if t > time_list[0]])

    def merge_teacher_student(self, teacher_list: List[List[int]], student_list: List[List[int]]) -> List[List[int]]:
        res = []
        for tea in teacher_list:
            for stu in student_list:
                if tea[0] <= stu[0] and tea[1] >= stu[1]:
                    res.append([stu[0], stu[1]])
                elif tea[0] >= stu[0] and tea[1] <= stu[1]:
                    res.append([tea[0], tea[1]])
                elif tea[0] <= stu[0] <= tea[1]:
                    res.append([stu[0], tea[1]])
                elif tea[0] >= stu[0] <= tea[1]:
                    res.append([tea[0], stu[1]])

        res = self.sort_list(res)
        return res


if __name__ == '__main__':
    li = [[11, 60], [4, 7]], [[2, 5], [13, 20], [6, 12]]
    s = Solution()
    print(s.merge_teacher_student(li[0], li[1]))
