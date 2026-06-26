class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = []

        temp = [matrix[0][0]]

        for i in range(1, len(matrix[0])):
            temp.append(temp[i - 1] + matrix[0][i])
        self.prefix.append(temp)

        for r in range(1, len(matrix)):
            temp = [matrix[r][0]]
            for c in range(1, len(matrix[0])):
                temp.append(temp[c - 1] + self.prefix[r - 1][c] + matrix[r][c] - self.prefix[r - 1][c - 1])
            self.prefix.append(temp)
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        print(self.prefixx)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)