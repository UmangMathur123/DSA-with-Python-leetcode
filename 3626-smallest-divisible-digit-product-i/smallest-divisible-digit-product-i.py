class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            a=n 
            num =1   
            while a:
                rem = a%10
                num *= rem
                a = a//10
            if num%t==0:
                return n
            n += 1
        