class Solution:
    def minMoves(self, nums: list[int]) -> int:
        target = max(nums)
        return sum(target - num for num in nums)
