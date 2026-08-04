class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        c = []
        a = min(nums)
        b = max(nums)
        for i in range(a+1,b):
            if i not in nums:
                c.append(i)
        return c
