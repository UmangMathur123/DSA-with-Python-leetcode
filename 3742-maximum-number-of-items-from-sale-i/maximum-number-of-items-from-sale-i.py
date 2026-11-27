
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:

        dp = [0] * (budget + 1)

        min_price = min(price for factor, price in items)

        for factor, price in items:

            count = 0

            for other_factor, other_price in items:
                if other_factor % factor == 0:
                    count += 1

            for j in range(budget, price - 1, -1):
                dp[j] = max(dp[j], dp[j - price] + count)

        ans = 0

        for i in range(budget + 1):
            extra = (budget - i) // min_price
            ans = max(ans, dp[i] + extra)

        return ans
