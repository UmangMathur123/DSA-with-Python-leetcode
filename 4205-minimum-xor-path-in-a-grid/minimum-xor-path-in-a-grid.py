class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        L = len(grid[0])
        arr = [[False] * 1024 for _ in range(L)]
        
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                nxt = [False] * 1024
                for k in range(1024):
                    if arr[j][k] or (j > 0 and arr[j-1][k]) or (i == 0 and j == 0 and k == 0):
                        nxt[k ^ val] = True
                arr[j] = nxt
                
        return next(ans for ans, ok in enumerate(arr[-1]) if ok)
