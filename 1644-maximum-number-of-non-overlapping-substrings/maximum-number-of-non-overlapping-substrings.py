class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)

        # First and last occurrence of every character
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        intervals = []

        # Try to create a valid interval starting
        # at the first occurrence of each character.
        for c in range(26):
            if first[c] == n:
                continue

            l = first[c]
            r = last[c]
            valid = True

            i = l
            while i <= r:
                idx = ord(s[i]) - ord('a')

                # This character occurs before l,
                # so the substring cannot contain all of it.
                if first[idx] < l:
                    valid = False
                    break

                # Expand interval if necessary
                r = max(r, last[idx])
                i += 1

            if valid:
                intervals.append((l, r))

        # Sort by ending position.
        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1

        # Greedily choose intervals that finish earliest.
        for l, r in intervals:
            if l > prev_end:
                result.append(s[l:r + 1])
                prev_end = r

        return result