class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total

        n = len(nums)

        arr = sorted(nums, key=lambda x: (digit_sum(x), x))

        pos = {num: i for i, num in enumerate(nums)}

        target = [pos[num] for num in arr]

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or target[i] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = target[j]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps