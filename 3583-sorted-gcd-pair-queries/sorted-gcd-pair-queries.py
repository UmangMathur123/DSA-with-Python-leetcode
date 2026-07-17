from typing import List
from bisect import bisect_left

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        # Frequency of each value
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # cnt[d] = how many numbers are divisible by d
        cnt = [0] * (mx + 1)
        for d in range(1, mx + 1):
            for multiple in range(d, mx + 1, d):
                cnt[d] += freq[multiple]

        # exact[d] = number of pairs whose gcd is exactly d
        exact = [0] * (mx + 1)
        for d in range(mx, 0, -1):
            pairs = cnt[d] * (cnt[d] - 1) // 2
            multiple = 2 * d
            while multiple <= mx:
                pairs -= exact[multiple]
                multiple += d
            exact[d] = pairs

        # Prefix count of sorted gcd values
        prefix = []
        values = []
        total = 0
        for d in range(1, mx + 1):
            if exact[d]:
                total += exact[d]
                prefix.append(total)
                values.append(d)

        # Answer queries
        ans = []
        for q in queries:
            idx = bisect_left(prefix, q + 1)
            ans.append(values[idx])

        return ans