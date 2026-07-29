from collections import Counter

class Solution:
    def __init__(self):
        self.MAX = 10**6 + 1

    def smallestPalindrome(self, s: str, k: int) -> str:
        count = Counter(s)

        halfCount = [0] * 26
        mid = ""

        for ch, freq in count.items():
            halfCount[ord(ch) - ord("a")] = freq // 2
            if freq % 2:
                mid = ch

        if self.countWays(halfCount) < k:
            return ""

        left = []
        halfLen = sum(halfCount)

        for _ in range(halfLen):
            for i in range(26):
                if halfCount[i] == 0:
                    continue

                halfCount[i] -= 1
                ways = self.countWays(halfCount)

                if ways >= k:
                    left.append(chr(i + ord("a")))
                    break

                k -= ways
                halfCount[i] += 1

        left = "".join(left)
        return left + mid + left[::-1]

    def countWays(self, cnt):
        total = sum(cnt)
        ans = 1

        for f in cnt:
            ans *= self.nCr(total, f)
            if ans >= self.MAX:
                return self.MAX
            total -= f

        return ans

    def nCr(self, n, r):
        r = min(r, n - r)
        ans = 1

        for i in range(1, r + 1):
            ans = ans * (n - i + 1) // i
            if ans >= self.MAX:
                return self.MAX

        return ans