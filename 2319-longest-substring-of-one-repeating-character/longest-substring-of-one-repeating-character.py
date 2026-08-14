from typing import List

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:

        n = len(s)

        # Each node stores:
        # left_char  = first character
        # right_char = last character
        # prefix     = longest same-character prefix
        # suffix     = longest same-character suffix
        # best       = longest repeating substring inside this range

        tree = [None] * (4 * n)

        def merge(left, right):
            if left is None:
                return right
            if right is None:
                return left

            lchar, rchar, lp, ls, lb, llen = left
            l2char, r2char, rp, rs, rb, rlen = right

            left_char = lchar
            right_char = r2char

            prefix = lp
            suffix = rs
            best = max(lb, rb)

            # If boundary characters are same,
            # suffix of left + prefix of right can form a longer group
            if rchar == l2char:
                best = max(best, ls + rp)

                if lp == llen:
                    prefix = llen + rp

                if rs == rlen:
                    suffix = rlen + ls

            return (
                left_char,
                right_char,
                prefix,
                suffix,
                best,
                llen + rlen
            )

        def build(node, start, end):
            if start == end:
                tree[node] = (s[start], s[start], 1, 1, 1, 1)
                return

            mid = (start + end) // 2

            build(node * 2, start, mid)
            build(node * 2 + 1, mid + 1, end)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, start, end, idx, ch):
            if start == end:
                tree[node] = (ch, ch, 1, 1, 1, 1)
                return

            mid = (start + end) // 2

            if idx <= mid:
                update(node * 2, start, mid, idx, ch)
            else:
                update(node * 2 + 1, mid + 1, end, idx, ch)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        build(1, 0, n - 1)

        ans = []

        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)

            # best value of root = answer for whole string
            ans.append(tree[1][4])

        return ans