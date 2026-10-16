from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        bit1 = [0] * (n + 2)
        bit2 = [0] * (n + 2)

        def update(bit, i, val):
            while i <= n:
                bit[i] = (bit[i] + val) % MOD
                i += i & -i

        def range_add(l, r, val):
            if l > r:
                return
            update(bit1, l, val)
            update(bit1, r + 1, -val)
            update(bit2, l, val * (l - 1))
            update(bit2, r + 1, -val * r)

        def query(bit, i):
            s = 0
            while i > 0:
                s = (s + bit[i]) % MOD
                i -= i & -i
            return s

        def prefix_sum(i):
            return (i * query(bit1, i) - query(bit2, i)) % MOD

        def range_sum(l, r):
            return (prefix_sum(r) - prefix_sum(l - 1)) % MOD

        last = {}
        curve = 0
        ans = 0

        for i, x in enumerate(nums, 1):
            j = last.get(x, 0) + 1

            s = range_sum(j, i)
            increase = (2 * s + i - j + 1) % MOD

            curve = (curve + increase) % MOD
            ans = (ans + curve) % MOD

            range_add(j, i, 1)
            last[x] = i

        return ans