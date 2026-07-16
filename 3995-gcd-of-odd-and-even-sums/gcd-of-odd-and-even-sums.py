class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even = 0
        odd = 0
        for i in range(1, 2*n+1):
            if i%2==0:
                even += i
            else:
                odd+=i
        while even:
            odd, even = even, odd%even
        return odd
        