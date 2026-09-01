from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        # Find S and number every L
        start = None
        litter_id = {}
        k = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter_id[(i, j)] = k
                    k += 1

        # No litter -> already done
        if k == 0:
            return 0

        all_mask = (1 << k) - 1

        # (row, col, remaining_energy, collected_mask)
        q = deque()
        q.append((start[0], start[1], energy, 0))

        # visited states
        visited = set()
        visited.add((start[0], start[1], energy, 0))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        moves = 0

        while q:
            size = len(q)

            for _ in range(size):
                r, c, e, mask = q.popleft()

                if mask == all_mask:
                    return moves

                # If we are on a reset cell, energy is full
                if classroom[r][c] == 'R':
                    e = energy

                # Can't move with zero energy
                if e == 0:
                    continue

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # Outside grid
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    # Obstacle
                    if classroom[nr][nc] == 'X':
                        continue

                    ne = e - 1
                    nmask = mask

                    # Collect litter
                    if classroom[nr][nc] == 'L':
                        idx = litter_id[(nr, nc)]
                        nmask |= (1 << idx)

                    # Reset energy on R
                    if classroom[nr][nc] == 'R':
                        ne = energy

                    state = (nr, nc, ne, nmask)

                    if state not in visited:
                        visited.add(state)
                        q.append(state)

            moves += 1

        return -1