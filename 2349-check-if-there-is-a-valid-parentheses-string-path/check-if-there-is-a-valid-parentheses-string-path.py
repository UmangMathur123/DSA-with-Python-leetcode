class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Total length of any valid path must be even
        if (m + n - 1) % 2 != 0:
            return False
            
        memo = {}
        
        def dfs(r, c, balance):
            # Update balance based on the current cell
            balance += 1 if grid[r][c] == '(' else -1
            
            # If balance drops below 0, this path is invalid
            if balance < 0:
                return False
                
            # Remaining steps to reach the bottom-right cell
            rem_steps = (m - 1 - r) + (n - 1 - c)
            
            # If current balance exceeds remaining steps, we can't reach 0
            if balance > rem_steps:
                return False
                
            # Base case: arrived at the bottom-right cell
            if r == m - 1 and c == n - 1:
                return balance == 0
                
            # Check memoization cache
            state = (r, c, balance)
            if state in memo:
                return memo[state]
                
            # Move Down or Move Right
            res = False
            if r + 1 < m:
                res = res or dfs(r + 1, c, balance)
            if c + 1 < n:
                res = res or dfs(r, c + 1, balance)
                
            memo[state] = res
            return res
            
        return dfs(0, 0, 0)
