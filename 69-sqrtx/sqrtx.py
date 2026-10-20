class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
            
        left, right = 1, x // 2
        ans = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            
            if square == x:
                return mid
            elif square < x:
                ans = mid      # mid could be the potential floor square root
                left = mid + 1  # Try to find a larger value
            else:
                right = mid - 1 # mid is too large, search lower half
                
        return ans
