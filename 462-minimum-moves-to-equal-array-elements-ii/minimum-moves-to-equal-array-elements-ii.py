class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        
        moves = 0
        i, j = 0, len(nums) - 1
        
        while i < j:
            moves += nums[j] - nums[i]
            i += 1
            j -= 1
            
        return moves
