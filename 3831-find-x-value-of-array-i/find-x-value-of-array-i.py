from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        # dp[r] = number of subarrays ending at the previous position
        # whose product % k == r
        dp = [0] * k

        # ans[r] = number of all subarrays whose product % k == r
        ans = [0] * k

        for num in nums:
            rem = num % k

            new_dp = [0] * k

            # Start a new subarray containing only nums[i]
            new_dp[rem] += 1

            # Extend every subarray ending at the previous position
            for r in range(k):
                if dp[r]:
                    new_rem = (r * rem) % k
                    new_dp[new_rem] += dp[r]

            # Add all subarrays ending at current position
            for r in range(k):
                ans[r] += new_dp[r]

            dp = new_dp

        return ans