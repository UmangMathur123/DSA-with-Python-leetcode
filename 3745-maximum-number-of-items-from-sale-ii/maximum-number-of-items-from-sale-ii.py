from collections import Counter
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        freq = Counter(factor for factor, _ in items)
        
        # Step 1: Sieve approach to calculate free bonus items for each factor
        bonus = [0] * (n + 1)
        for i in range(1, n + 1):
            if freq[i] == 0:
                continue
            for j in range(i, n + 1, i):
                bonus[i] += freq[j]
            bonus[i] -= 1  # Remove the item's own contribution
            
        # Step 2: Sort items by price in ascending order
        items.sort(key=lambda x: x[1])
        cheapest = items[0][1]
        res = 0
        
        # Step 3: Greedily buy pairs while price < 2 * cheapest
        for factor, price in items:
            if price >= cheapest * 2:
                break
            pairs = min(bonus[factor], budget // price)
            res += pairs * 2
            budget -= pairs * price
            
        # Step 4: Spend remaining budget on the cheapest item
        res += budget // cheapest
        return res