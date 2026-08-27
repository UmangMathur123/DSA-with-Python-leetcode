class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        ans = [''] * n

        # Build prefix equal to target as long as possible
        for i in range(n):
            t = ord(target[i]) - ord('a')

            # Use same character if possible
            if freq[t] > 0:
                ans[i] = target[i]
                freq[t] -= 1
            else:
                # We cannot continue equal.
                # Try to put the smallest greater character here.
                for c in range(t + 1, 26):
                    if freq[c] > 0:
                        ans[i] = chr(c + ord('a'))
                        freq[c] -= 1

                        # Fill rest in smallest order
                        pos = i + 1
                        for x in range(26):
                            while freq[x] > 0:
                                ans[pos] = chr(x + ord('a'))
                                pos += 1
                                freq[x] -= 1

                        return ''.join(ans)

                # No greater character here.
                # Need to backtrack.
                break

        # Backtrack: change an earlier equal character
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        for i in range(n - 1, -1, -1):
            # Remove target[0:i] from available characters
            temp = freq[:]

            valid = True
            for j in range(i):
                c = ord(target[j]) - ord('a')
                if temp[c] == 0:
                    valid = False
                    break
                temp[c] -= 1

            if not valid:
                continue

            t = ord(target[i]) - ord('a')

            # Find smallest character > target[i]
            for c in range(t + 1, 26):
                if temp[c] > 0:
                    result = target[:i] + chr(c + ord('a'))
                    temp[c] -= 1

                    # Smallest possible suffix
                    for x in range(26):
                        result += chr(x + ord('a')) * temp[x]

                    return result

        return ""