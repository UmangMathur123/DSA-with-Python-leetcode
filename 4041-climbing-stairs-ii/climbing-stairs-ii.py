class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            cost_i = costs[i - 1]
            
            if i - 1 >= 0:
                dp[i] = min(dp[i], dp[i - 1] + cost_i + 1)
            if i - 2 >= 0:
                dp[i] = min(dp[i], dp[i - 2] + cost_i + 4)
            if i - 3 >= 0:
                dp[i] = min(dp[i], dp[i - 3] + cost_i + 9)
                
        return dp[n]