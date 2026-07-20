class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        # 2D grid ko 1D list mein convert
        arr = []
        for row in grid:
            arr.extend(row)

        # k shifts
        k = k % (m * n)

        arr = arr[-k:] + arr[:-k]

        # 1D list ko wapas 2D grid mein convert
        result = []
        index = 0

        for i in range(m):
            row = []
            for j in range(n):
                row.append(arr[index])
                index += 1
            result.append(row)

        return result