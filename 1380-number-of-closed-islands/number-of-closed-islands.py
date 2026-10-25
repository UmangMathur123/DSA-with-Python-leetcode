from collections import deque
from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue = deque([(i, j)])
                    grid[i][j] = 1
                    closed = True

                    while queue:
                        x, y = queue.popleft()

                        if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                            closed = False

                        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            nx, ny = x + dx, y + dy

                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                                grid[nx][ny] = 1
                                queue.append((nx, ny))

                    if closed:
                        count += 1

        return count