class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # Initialize the entire grid filled with obstacles ('#')
        grid = [["#"] * n for _ in range(m)]
        
        # Free up the entire top row (Row 0)
        for j in range(n):
            grid[0][j] = "."
            
        # Free up the entire right column (Column n - 1)
        for i in range(m):
            grid[i][n - 1] = "."
            
        # Convert each row list of characters into a string
        return ["".join(row) for row in grid]
