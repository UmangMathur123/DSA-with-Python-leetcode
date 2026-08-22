class Solution:
    def checkDivisibility(self, n: int) -> bool:
        n_copy = n
        s = 0
        p = 1
        while n_copy>0:
            rem = n_copy%10
            s+=rem
            p*=rem
            n_copy //= 10
        result = s+p
        return n%result==0
        