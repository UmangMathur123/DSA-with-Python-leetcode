class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        i = -1
        return (nums[i] -1) * (nums[i-1] -1)
