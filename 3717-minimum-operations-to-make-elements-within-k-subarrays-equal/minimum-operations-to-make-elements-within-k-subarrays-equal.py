from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        
        left_heap = []   
        right_heap = []  
        
        left_sum = 0
        right_sum = 0
        
        left_size = 0
        right_size = 0
        
        to_remove = defaultdict(int)
        
        def prune(heap, is_left):
            nonlocal left_size, right_size
            while heap:
                val = heap[0] if not is_left else -heap[0]
                if to_remove[val] > 0:
                    to_remove[val] -= 1
                    heappop(heap)
                else:
                    break
        
        def balance():
            nonlocal left_sum, right_sum, left_size, right_size
            while left_size > right_size + 1:
                prune(left_heap, True)
                val = -heappop(left_heap)
                left_sum -= val
                left_size -= 1
                heappush(right_heap, val)
                right_sum += val
                right_size += 1
                prune(left_heap, True)
            
            while left_size < right_size:
                prune(right_heap, False)
                val = heappop(right_heap)
                right_sum -= val
                right_size -= 1
                heappush(left_heap, -val)
                left_sum += val
                left_size += 1
                prune(right_heap, False)

        def add_num(num):
            nonlocal left_sum, right_sum, left_size, right_size
            if not left_heap or num <= -left_heap[0]:
                heappush(left_heap, -num)
                left_sum += num
                left_size += 1
            else:
                heappush(right_heap, num)
                right_sum += num
                right_size += 1
            balance()

        def remove_num(num):
            nonlocal left_sum, right_sum, left_size, right_size
            to_remove[num] += 1
            if num <= -left_heap[0]:
                left_sum -= num
                left_size -= 1
                if num == -left_heap[0]:
                    prune(left_heap, True)
            else:
                right_sum -= num
                right_size -= 1
                if num == right_heap[0]:
                    prune(right_heap, False)
            balance()

        cost = [float('inf')] * n
        
        for i in range(n):
            add_num(nums[i])
            if i >= x:
                remove_num(nums[i - x])
            
            if i >= x - 1:
                prune(left_heap, True)
                median = -left_heap[0]
                current_cost = (median * left_size - left_sum) + (right_sum - median * right_size)
                cost[i - x + 1] = current_cost
                
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 0
            
        for i in range(n - 1, -1, -1):
            for j in range(1, k + 1):
                dp[i][j] = dp[i + 1][j]
                if i + x <= n and cost[i] != float('inf'):
                    dp[i][j] = min(dp[i][j], cost[i] + dp[i + x][j - 1])
                    
        return dp[0][k]
