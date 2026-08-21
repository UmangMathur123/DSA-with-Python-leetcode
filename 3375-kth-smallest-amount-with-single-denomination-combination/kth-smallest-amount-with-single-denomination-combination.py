class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        from math import gcd

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0
            m = len(coins)

            for mask in range(1, 1 << m):
                L = 1
                bits = 0

                for i in range(m):
                    if mask & (1 << i):
                        L = lcm(L, coins[i])

                        if L > x:
                            break

                        bits += 1

                if L <= x:
                    if bits % 2 == 1:
                        total += x // L
                    else:
                        total -= x // L

            return total

        low = 1
        high = min(coins) * k

        while low < high:
            mid = (low + high) // 2

            if count(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low