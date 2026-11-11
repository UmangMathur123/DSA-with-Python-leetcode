class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        common = min(need1, need2)
        rem1 = need1 - common
        rem2 = need2 - common
        
        common_cost = common * min(costBoth, cost1 + cost2)
        rem1_cost = rem1 * min(cost1, costBoth)
        rem2_cost = rem2 * min(cost2, costBoth)
        
        return common_cost + rem1_cost + rem2_cost
