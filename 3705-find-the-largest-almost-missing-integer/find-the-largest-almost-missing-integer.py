class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count = {}

        # Every subarray of size k
        for i in range(len(nums) - k + 1):
            window = set(nums[i:i + k])

            # Count each number only once per window
            for x in window:
                count[x] = count.get(x, 0) + 1

        ans = -1

        for x, freq in count.items():
            if freq == 1:
                ans = max(ans, x)

        return ans