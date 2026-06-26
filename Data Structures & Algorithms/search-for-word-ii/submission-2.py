class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        memory = set()
        def dfs(i, j, c, word):
            if c == len(word):
                return True
            if (i, j) in memory or i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[c]:
                return False
            
            memory.add((i, j))

            found = dfs(i - 1, j, c + 1, word) or dfs(i + 1, j, c + 1, word) or dfs(i, j - 1, c + 1, word) or dfs(i, j + 1, c + 1, word)

            memory.remove((i, j))
            return found

        ans = []
        for word in words:
            found = False
            for i in range(len(board)):
                if found:
                    break
                for j in range(len(board[0])):
                    if dfs(i, j, 0, word):
                        ans.append(word)
                        found = True
                        break
        
        return ans