class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)

        new_parent = parent[:]
        last_seen = [-1] * 26

        # स्टेप 1: हर नोड का नया पैरेंट ढूंढना (DFS + Backtracking)
        def dfs_parents(u: int) -> None:
            c = ord(s[u]) - ord('a')
            prev = last_seen[c]
            
            if prev != -1:
                new_parent[u] = prev
            
            last_seen[c] = u
            for v in adj[u]:
                dfs_parents(v)
            last_seen[c] = prev  # Backtrack

        dfs_parents(0)

        # स्टेप 2: नए पैरेंट्स के हिसाब से नया ट्री बनाना
        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)

        # स्टेप 3: हर नोड के सबट्री का साइज निकालना
        ans = [0] * n
        def dfs_size(u: int) -> int:
            size = 1
            for v in new_adj[u]:
                size += dfs_size(v)
            ans[u] = size
            return size

        dfs_size(0)
        return ans
