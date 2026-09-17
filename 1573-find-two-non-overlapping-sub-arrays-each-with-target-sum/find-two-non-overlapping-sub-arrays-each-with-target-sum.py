class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')

        # best[i] = index i tak target sum wale
        # shortest subarray ki minimum length
        best = [INF] * n

        left = 0
        current_sum = 0
        min_len = INF
        answer = INF

        for right in range(n):
            current_sum += arr[right]

            while current_sum > target:
                current_sum -= arr[left]
                left += 1

            if current_sum == target:
                curr_len = right - left + 1

                # left se pehle koi target subarray mila ho
                if left > 0 and best[left - 1] != INF:
                    answer = min(answer, curr_len + best[left - 1])

                min_len = min(min_len, curr_len)

            best[right] = min_len

        return -1 if answer == INF else answer