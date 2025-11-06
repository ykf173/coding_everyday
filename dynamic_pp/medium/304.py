from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        if matrix != [[]]:
            rowNum, colNum = len(matrix), len(matrix[0])
            for i in range(1, rowNum):
                self.matrix[i][0] += self.matrix[i - 1][0]

            for i in range(1, colNum):
                self.matrix[0][i] += self.matrix[0][i - 1]

            for i in range(1, rowNum):
                for j in range(1, colNum):
                    self.matrix[i][j] += self.matrix[i - 1][j] + self.matrix[i][j - 1] - self.matrix[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.matrix == [[]]:
            return 0
        if not row1 and col1:
            return self.matrix[row2][col2] - self.matrix[row2][col1 - 1]
        elif row1 and not col1:
            return self.matrix[row2][col2] - self.matrix[row1 - 1][col2]
        elif not row1 and not col1:
            return self.matrix[row2][col2]

        return self.matrix[row2][col2] - self.matrix[row1 - 1][col2] - self.matrix[row2][col1 - 1] + \
               self.matrix[row1 - 1][col1 - 1]

# Your NumMatrix object will be instantiated and called as such:

matrix = [[]
]
obj = NumMatrix(matrix)
print(obj.sumRegion(2, 1, 4, 3))
print(obj.sumRegion(1, 1, 2, 2))
print(obj.sumRegion(1, 2, 2, 4))
print(obj.sumRegion(1, 0, 2, 3))
print(obj.sumRegion(0, 1, 2, 2))
print(obj.sumRegion(0, 0, 1, 1))
print(obj.sumRegion(0, 0, 0, 1))

