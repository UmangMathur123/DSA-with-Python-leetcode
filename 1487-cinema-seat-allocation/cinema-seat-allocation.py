class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}

        for r, s in reservedSeats:
            if r not in rows:
                rows[r] = set()
            rows[r].add(s)

        # Initially, every empty row can fit 2 families
        ans = (n - len(rows)) * 2

        for seats in rows.values():
            count = 0

            # Left block: 2,3,4,5
            left = all(s not in seats for s in [2, 3, 4, 5])

            # Middle block: 4,5,6,7
            middle = all(s not in seats for s in [4, 5, 6, 7])

            # Right block: 6,7,8,9
            right = all(s not in seats for s in [6, 7, 8, 9])

            if left:
                count += 1

            if right:
                count += 1

            # If neither left nor right is available,
            # middle can be used alone.
            if count == 0 and middle:
                count = 1

            ans += count

        return ans