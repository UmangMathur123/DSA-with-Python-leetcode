class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        Maxcandies= max(candies)
        ans=[]
        for i in candies:
            if(i+extraCandies)>=Maxcandies:
                ans.append(True)
            else:
                ans.append(False)
        return ans