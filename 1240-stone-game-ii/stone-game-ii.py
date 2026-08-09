class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # suffix[i] = total stones from i to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = piles[i] + suffix[i + 1]

        # dp(i, M) = maximum stones current player can get
        # starting from index i with current M
        from functools import lru_cache

        @lru_cache(None)
        def dp(i, M):
            if i >= n:
                return 0

            # If we can take all remaining piles
            if i + 2 * M >= n:
                return suffix[i]

            best = 0

            # Take X piles, where 1 <= X <= 2*M
            for X in range(1, 2 * M + 1):
                # Stones current player gets
                # = all remaining stones - what opponent can get
                opponent = dp(i + X, max(M, X))
                current = suffix[i] - opponent

                best = max(best, current)

            return best

        return dp(0, 1)