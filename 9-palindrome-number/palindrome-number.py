class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = x
        y = 0
        n = len(str(x))
        for i in range(n):
            rem = a%10
            y = y*10+rem
            a = a//10
        if x==y:
            return True
        else:
            return False

