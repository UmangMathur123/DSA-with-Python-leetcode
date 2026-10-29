class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        parent = [0] * n
        depth = [0] * n
        heavy = [-1] * n
        size = [0] * n
        
        stack = [(0, -1, 0)]
        order = []
        while stack:
            u, p, d = stack.pop()
            parent[u] = p
            depth[u] = d
            size[u] = 1
            order.append(u)
            for v in adj[u]:
                if v != p:
                    stack.append((v, u, d + 1))
                    
        for u in reversed(order):
            max_size = 0
            for v in adj[u]:
                if v != parent[u]:
                    size[u] += size[v]
                    if size[v] > max_size:
                        max_size = size[v]
                        heavy[u] = v
                        
        head = [0] * n
        pos = [0] * n
        cur_pos = 0
        
        stack = [(0, 0)]
        while stack:
            u, h = stack.pop()
            head[u] = h
            pos[u] = cur_pos
            cur_pos += 1
            
            for v in adj[u]:
                if v != parent[u] and v != heavy[u]:
                    stack.append((v, v))
            if heavy[u] != -1:
                stack.append((heavy[u], h))
                
        tree = [0] * (2 * n)
        
        for i in range(n):
            tree[n + pos[i]] = 1 << (ord(s[i]) - ord('a'))
            
        for i in range(n - 1, 0, -1):
            tree[i] = tree[2 * i] ^ tree[2 * i + 1]
            
        def seg_update(p, val):
            p += n
            tree[p] = val
            while p > 1:
                tree[p >> 1] = tree[p] ^ tree[p ^ 1]
                p >>= 1
                
        def seg_query(l, r):
            res = 0
            l += n
            r += n + 1
            while l < r:
                if l & 1:
                    res ^= tree[l]
                    l += 1
                if r & 1:
                    r -= 1
                    res ^= tree[r]
                l >>= 1
                r >>= 1
            return res
            
        def query_path(u, v):
            res_mask = 0
            while head[u] != head[v]:
                if depth[head[u]] > depth[head[v]]:
                    u, v = v, u
                res_mask ^= seg_query(pos[head[v]], pos[v])
                v = parent[head[v]]
            if depth[u] > depth[v]:
                u, v = v, u
            res_mask ^= seg_query(pos[u], pos[v])
            return res_mask

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                ui = int(parts[1])
                c = parts[2]
                mask = 1 << (ord(c) - ord('a'))
                seg_update(pos[ui], mask)
            else:
                ui = int(parts[1])
                vi = int(parts[2])
                path_mask = query_path(ui, vi)
                ans.append((path_mask & (path_mask - 1)) == 0)
                
        return ans
