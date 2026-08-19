class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp=n
        prd=1
        summ=0
        while temp>0:
            r=temp%10
            temp//=10
            prd=prd*r
            summ=summ+r
        return prd-summ
