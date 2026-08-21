class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 0 and n % 2 == 0:
            n //= 2

        return n == 1