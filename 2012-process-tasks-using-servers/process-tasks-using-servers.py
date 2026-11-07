import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        # available: (weight, index)
        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)
        
        # busy: (free_time, weight, index)
        busy = []
        ans = []
        
        t = 0
        for j, task_time in enumerate(tasks):
            # Fast-forward time to the arrival time of the current task if time lagged behind
            t = max(t, j)
            
            # If no servers are available, jump directly to when the earliest busy server frees up
            if not available:
                t = max(t, busy[0][0])
                
            # Move all servers that became free at or before current time 't' to the available heap
            while busy and busy[0][0] <= t:
                free_time, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))
                
            # Assign the task to the best available server
            weight, idx = heapq.heappop(available)
            ans.append(idx)
            
            # Put the server into the busy heap with its new release time
            heapq.heappush(busy, (t + task_time, weight, idx))
            
        return ans
