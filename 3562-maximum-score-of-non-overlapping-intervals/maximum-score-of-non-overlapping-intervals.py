from typing import List
from bisect import bisect_left


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:

        n = len(intervals)

        # Add original index
        arr = [
            [l, r, w, i]
            for i, (l, r, w) in enumerate(intervals)
        ]

        # Sort by right endpoint
        arr.sort(key=lambda x: x[1])

        # All right endpoints
        rights = [x[1] for x in arr]

        # prev[i] = last interval whose right < current left
        prev = [0] * n

        for i in range(n):
            left = arr[i][0]

            # Number of intervals having right < left
            p = bisect_left(rights, left)

            # Convert to dp index
            prev[i] = p

        # dp[k][i]:
        # best answer using at most k intervals
        # from first i sorted intervals
        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        for k in range(1, 5):

            for i in range(1, n + 1):

                # Option 1: Don't take current interval
                best_score, best_indices = dp[k][i - 1]

                # Current interval
                l, r, w, original_index = arr[i - 1]

                # Option 2: Take current interval
                p = prev[i - 1]

                old_score, old_indices = dp[k - 1][p]

                take_score = old_score + w
                take_indices = tuple(
                    sorted(old_indices + (original_index,))
                )

                # Compare
                if take_score > best_score:
                    dp[k][i] = (take_score, take_indices)

                elif take_score < best_score:
                    dp[k][i] = (best_score, best_indices)

                else:
                    # Same score -> lexicographically smaller
                    if take_indices < best_indices:
                        dp[k][i] = (take_score, take_indices)
                    else:
                        dp[k][i] = (best_score, best_indices)

        # We can choose UP TO 4 intervals
        answer_score = 0
        answer = ()

        for k in range(5):

            score, indices = dp[k][n]

            if score > answer_score:
                answer_score = score
                answer = indices

            elif score == answer_score:
                if indices < answer:
                    answer = indices

        return list(answer)