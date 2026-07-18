class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        for r in range(9):
            rowSeen = set()
            colSeen = set()
            for c in range(9):
                if board[r][c] != '.' and board[r][c] in rowSeen: return False
                elif board[r][c] != '.': rowSeen.add(board[r][c])
                if board[c][r] != '.' and board[c][r] in colSeen: return False
                elif board[c][r] != '.': colSeen.add(board[c][r])

        for i in range(0, 9, 3):
            for k in range(0, 9, 3):
                seen = set()
                for r in range(3):
                    for c in range(3):
                        if board[i + r][k + c] != '.' and board[i + r][k + c] in seen: return False
                        elif board[i + r][k + c] != '.': seen.add(board[i + r][k + c])
        return True