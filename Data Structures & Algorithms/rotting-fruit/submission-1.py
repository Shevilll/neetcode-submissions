class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = deque()
        res = -1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))


        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in neighbors:
                    newr, newc = r + dr, c + dc
                    if min(newr, newc) < 0 or newr == ROWS or newc == COLS or grid[newr][newc] == 0 or grid[newr][newc] == 2:
                        continue
                    grid[newr][newc] = 2
                    queue.append((newr, newc))
            res += 1
                
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
                
        return res