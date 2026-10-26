class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        divisible_islands_count = 0
        
        # Directions for 4-directional movement: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for i in range(m):
            for j in range(n):
                # If we encounter a cell with value > 0, it's a new island
                if grid[i][j] > 0:
                    island_sum = 0
                    queue = [(i, j)]
                    island_sum += grid[i][j]
                    grid[i][j] = 0  # Mark as visited by sinking the land
                    
                    # Standard BFS to traverse the entire island
                    while queue:
                        r, c = queue.pop(0)
                        
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            
                            # Check boundaries and if the neighboring cell is land
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                island_sum += grid[nr][nc]
                                grid[nr][nc] = 0  # Mark as visited
                                queue.append((nr, nc))
                    
                    # Check if the total island value is divisible by k
                    if island_sum % k == 0:
                        divisible_islands_count += 1
                        
        return divisible_islands_count
