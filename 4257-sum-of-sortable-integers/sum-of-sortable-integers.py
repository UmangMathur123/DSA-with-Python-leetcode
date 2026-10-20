class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        target = sorted(nums)
        
        # 1. Find all possible block sizes (divisors of n)
        divisors = []
        d = 1
        while d * d <= n:
            if n % d == 0:
                divisors.append(d)
                if d * d != n:
                    divisors.append(n // d)
            d += 1
            
        ans = 0
        
        # 2. Check each block size k
        for k in divisors:
            is_sortable = True
            
            for start in range(0, n, k):
                # Slices for the current block
                a = nums[start : start + k]
                b = target[start : start + k]
                
                # Check 1: Must have the exact same elements
                if sorted(a) != b:
                    is_sortable = False
                    break
                
                # Check 2: Must be a valid cyclic rotation
                drops = 0
                for i in range(k - 1):
                    if a[i] > a[i + 1]:
                        drops += 1
                
                if drops > 1 or (drops == 1 and a[-1] > a[0]):
                    is_sortable = False
                    break
            
            if is_sortable:
                ans += k
                
        return ans
