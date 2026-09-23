class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        target = total - x
        
        # If we need to remove everything
        if target == 0:
            return len(nums)
        
        # Impossible if target is negative
        if target < 0:
            return -1
        
        left = 0
        curr_sum = 0
        max_len = -1
        
        for right in range(len(nums)):
            curr_sum += nums[right]
            
            # Reduce window if sum becomes too large
            while curr_sum > target:
                curr_sum -= nums[left]
                left += 1
            
            # Found a subarray with required sum
            if curr_sum == target:
                max_len = max(max_len, right - left + 1)
        
        if max_len == -1:
            return -1
        
        return len(nums) - max_len