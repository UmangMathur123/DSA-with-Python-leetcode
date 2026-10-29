class SegmentTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (4 * size)
        
    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = self.tree[2 * node] ^ self.tree[2 * node + 1]

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        return self.query(2 * node, start, mid, l, r) ^ self.query(2 * node + 1, mid + 1, end, l, r)

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
                
        seg_tree = SegmentTree(n)
        for i in range(n):
            mask = 1 << (ord(s[i]) - ord('a'))
            seg_tree.update(1, 0, n - 1, pos[i], mask)
            
        def query_path(u, v):
            res_mask = 0
            while head[u] != head[v]:
                if depth[head[u]] > depth[head[v]]:
                    u, v = v, u
                res_mask ^= seg_tree.query(1, 0, n - 1, pos[head[v]], pos[v])
                v = parent[head[v]]
            if depth[u] > depth[v]:
                u, v = v, u
            res_mask ^= seg_tree.query(1, 0, n - 1, pos[u], pos[v])
            return res_mask

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                ui = int(parts[1])
                c = parts[2]
                mask = 1 << (ord(c) - ord('a'))
                seg_tree.update(1, 0, n - 1, pos[ui], mask)
            else:
                ui = int(parts[1])
                vi = int(parts[2])
                path_mask = query_path(ui, vi)
                ans.append((path_mask & (path_mask - 1)) == 0)
                
        return ans
