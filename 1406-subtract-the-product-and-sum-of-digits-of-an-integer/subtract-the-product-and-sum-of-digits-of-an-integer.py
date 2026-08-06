class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp=n
        suum=0
        p=1
        while temp>0:
            r=temp%10
            temp//=10
            suum=suum+r
            p=p*r
        return p-suum

        