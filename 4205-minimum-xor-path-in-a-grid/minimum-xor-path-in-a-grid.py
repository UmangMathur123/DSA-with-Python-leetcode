class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        C = len(grid[0])
        dp = [[False] * 1024 for _ in range(C)]
        
        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                nxt = [False] * 1024
                for x in range(1024):
                    if dp[c][x] or (c > 0 and dp[c-1][x]) or (r == 0 and c == 0 and x == 0):
                        nxt[x ^ v] = True
                dp[c] = nxt
                
        return next(x for x, valid in enumerate(dp[-1]) if valid)

