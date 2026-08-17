class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:

        n = len(stoneValue)

        # Prefix sum
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        # Memoization table
        dp = [[-1] * n for _ in range(n)]

        def dfs(i, j):

            # Only one stone
            if i == j:
                return 0

            # Already calculated
            if dp[i][j] != -1:
                return dp[i][j]

            ans = 0

            left_sum = 0
            right_sum = prefix[j + 1] - prefix[i]

            for k in range(i, j):

                left_sum += stoneValue[k]
                right_sum -= stoneValue[k]

                # Left side is smaller
                if left_sum < right_sum:

                    # Pruning
                    if ans >= left_sum * 2:
                        continue

                    ans = max(
                        ans,
                        left_sum + dfs(i, k)
                    )

                # Right side is smaller
                elif left_sum > right_sum:

                    # Pruning
                    if ans >= right_sum * 2:
                        break

                    ans = max(
                        ans,
                        right_sum + dfs(k + 1, j)
                    )

                # Both are equal
                else:

                    ans = max(
                        ans,
                        left_sum + dfs(i, k),
                        right_sum + dfs(k + 1, j)
                    )

            dp[i][j] = ans
            return ans

        return dfs(0, n - 1)