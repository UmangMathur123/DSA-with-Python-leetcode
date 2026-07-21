class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = '1' + s + '1'

        ones = s.count('1')
        max_gain = 0

        # Store lengths of consecutive groups
        groups = []
        i = 0

        while i < len(t):
            j = i

            while j < len(t) and t[j] == t[i]:
                j += 1

            groups.append((t[i], j - i))
            i = j

        # Pattern: 0-block, 1-block, 0-block
        for i in range(1, len(groups) - 1):
            if groups[i][0] == '1':
                left_zero = groups[i - 1][1]
                right_zero = groups[i + 1][1]

                max_gain = max(max_gain, left_zero + right_zero)

        return ones + max_gain