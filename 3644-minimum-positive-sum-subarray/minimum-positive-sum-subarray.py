from typing import List


class Solution:

  def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
    n = len(nums)
    min_positive_sum = float('inf')

    # Iterate through all possible starting indices
    for i in range(n):
      current_sum = 0
      # Extend the subarray up to the maximum allowed length r
      for j in range(i, min(n, i + r)):
        current_sum += nums[j]
        length = j - i + 1

        # Check if the length is within [l, r] and the sum is strictly positive
        if length >= l and current_sum > 0:
          min_positive_sum = min(min_positive_sum, current_sum)

    return min_positive_sum if min_positive_sum != float('inf') else -1
