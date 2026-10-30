import heapq
from collections import defaultdict


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:



        adj = defaultdict(list)

        for u, v, w in edges:
            adj[u].append((v, w))

        # dist[node][count] = minimum cost
        # count represents consecutive occurrences
        dist = [[float('inf')] * (k + 1) for _ in range(n)]

        pq = [(0, 0, 1)]

        dist[0][1] = 0

        while pq:
            cost, node, count = heapq.heappop(pq)

            if node == n - 1:
                return cost

            if cost > dist[node][count]:
                continue

            for nei, weight in adj[node]:

                if labels[nei] == labels[node]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_cost = cost + weight

                if new_cost < dist[nei][new_count]:
                    dist[nei][new_count] = new_cost
                    heapq.heappush(
                        pq, (new_cost, nei, new_count)
                    )

        return -1