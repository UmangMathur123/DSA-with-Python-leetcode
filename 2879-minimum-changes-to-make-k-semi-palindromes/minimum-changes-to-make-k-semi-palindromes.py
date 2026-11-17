class Solution:

  def minimumChanges(self, s: str, k: int) -> int:
    n = len(s)

    # Precompute proper divisors for each length up to n
    divisors = [[] for _ in range(n + 1)]
    for length in range(1, n + 1):
      for d in range(1, length):
        if length % d == 0:
          divisors[length].append(d)

    # cost[i][j]: min changes to make s[i...j] (0-indexed) a semi-palindrome
    cost = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
      for j in range(i, n):
        length = j - i + 1
        sub = s[i : j + 1]
        min_changes_sub = float('inf')

        # Try every valid divisor d
        for d in divisors[length]:
          changes = 0
          # Check each of the d groups
          for group in range(d):
            left = group
            right = length - 1 - ((length - 1 - group) % d)
            # We can step through the group using pointers
            # Better: collect indices for this group
            indices = list(range(group, length, d))
            l_ptr, r_ptr = 0, len(indices) - 1
            while l_ptr < r_ptr:
              if sub[indices[l_ptr]] != sub[indices[r_ptr]]:
                changes += 1
              l_ptr += 1
              r_ptr -= 1
          min_changes_sub = min(min_changes_sub, changes)

        cost[i][j] = min_changes_sub

    # dp[i][j]: min changes to partition s[0...i] into j substrings
    dp = [[float('inf')] * (k + 1) for _ in range(n)]

    # Base case: 1 partition for prefix s[0...i]
    for i in range(n):
      dp[i][1] = cost[0][i]

    # Fill DP table
    for j in range(2, k + 1):
      for i in range(j - 1, n):
        for p in range(j - 2, i):
          dp[i][j] = min(dp[i][j], dp[p][j - 1] + cost[p + 1][i])

    return dp[n - 1][k]
