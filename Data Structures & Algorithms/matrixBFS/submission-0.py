class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        queue.append((0, 0))
        visited.add((0, 0))
        ROWS, COLS = len(grid), len(grid[0])
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        count = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return count
                for dr, dc in neighbors:
                    if min(r + dr, c + dc) < 0 or r + dr == ROWS or c + dc == COLS or grid[r + dr][c + dc] == 1 or (r + dr, c + dc) in visited:
                        continue
                    queue.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))
            count += 1
                

        return -1