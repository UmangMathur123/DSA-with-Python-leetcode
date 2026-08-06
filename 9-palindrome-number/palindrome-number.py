class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        rev = 0
        while x > 0:
            r = x % 10
            x //= 10
            rev = rev * 10 + r

        if rev == temp:
            return True
        else:
            return False