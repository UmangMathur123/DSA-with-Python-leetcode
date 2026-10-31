class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
        next_right = [[None] * n for _ in range(m)]
        next_down = [[None] * n for _ in range(m)]
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    next_right[i][j] = (i, j)
                else:
                    if i + 1 < m:
                        next_right[i][j] = next_down[i + 1][j]
                    else:
                        next_right[i][j] = None
                
                if grid[i][j] == 0:
                    next_down[i][j] = (i, j)
                else:
                    if j + 1 < n:
                        next_down[i][j] = next_right[i][j + 1]
                    else:
                        next_down[i][j] = None
                        
        dp_r = [[0] * n for _ in range(m)]
        dp_d = [[0] * n for _ in range(m)]
        
        dp_r[0][0] = 1
        dp_d[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    continue
                
                current_paths = (dp_r[i][j] + dp_d[i][j]) % MOD
                if i == 0 and j == 0:
                    current_paths = 1 
                
                if j + 1 < n:
                    dest = next_right[i][j + 1]
                    if dest is not None:
                        ni, nj = dest
                        dp_r[ni][nj] = (dp_r[ni][nj] + current_paths) % MOD
                        
                if i + 1 < m:
                    dest = next_down[i + 1][j]
                    if dest is not None:
                        ni, nj = dest
                        dp_d[ni][nj] = (dp_d[ni][nj] + current_paths) % MOD
                        
        return (dp_r[m - 1][n - 1] + dp_d[m - 1][n - 1]) % MOD
