from typing import List


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)

        # Segment tree size
        size = 1
        while size < n:
            size <<= 1

        # prod[node] = product of entire segment modulo k
        prod = [1] * (2 * size)

        # cnt[node][r] = number of non-empty prefixes
        # whose product % k == r
        cnt = [[0] * k for _ in range(2 * size)]

        # Build leaves
        for i, value in enumerate(nums):
            p = value % k
            node = size + i

            prod[node] = p
            cnt[node][p] = 1

        # Merge function
        def merge(a, b):
            pa, ca = a
            pb, cb = b

            new_prod = (pa * pb) % k
            new_cnt = ca[:]

            for r in range(k):
                new_cnt[(pa * r) % k] += cb[r]

            return new_prod, new_cnt

        # Build tree
        for node in range(size - 1, 0, -1):
            prod[node], cnt[node] = merge(
                (prod[node << 1], cnt[node << 1]),
                (prod[node << 1 | 1], cnt[node << 1 | 1])
            )

        # Point update
        def update(index, value):
            node = size + index
            p = value % k

            prod[node] = p
            cnt[node] = [0] * k
            cnt[node][p] = 1

            node >>= 1

            while node:
                prod[node], cnt[node] = merge(
                    (prod[node << 1], cnt[node << 1]),
                    (prod[node << 1 | 1], cnt[node << 1 | 1])
                )
                node >>= 1

        # Range query [left, right]
        def query(left, right):
            left += size
            right += size + 1

            left_prod = 1
            left_cnt = [0] * k

            right_prod = 1
            right_cnt = [0] * k

            while left < right:

                if left & 1:
                    left_prod, left_cnt = merge(
                        (left_prod, left_cnt),
                        (prod[left], cnt[left])
                    )
                    left += 1

                if right & 1:
                    right -= 1

                    right_prod, right_cnt = merge(
                        (prod[right], cnt[right]),
                        (right_prod, right_cnt)
                    )

                left >>= 1
                right >>= 1

            return merge(
                (left_prod, left_cnt),
                (right_prod, right_cnt)
            )

        # Process queries
        answer = []

        for index, value, start, x in queries:

            # Update persists for future queries
            update(index, value)

            # After removing prefix [0 ... start-1],
            # every possible remaining prefix corresponds
            # to one possible suffix removal.
            _, prefix_count = query(start, n - 1)

            answer.append(prefix_count[x])

        return answer