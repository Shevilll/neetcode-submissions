class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[matrix[i][0]] for i in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])):
                self.prefix[i].append(self.prefix[i][j - 1] + matrix[i][j])


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1, row2 + 1):
            ans += self.prefix[i][col2] - (self.prefix[i][col1 - 1] if col1 > 0 else 0)
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)