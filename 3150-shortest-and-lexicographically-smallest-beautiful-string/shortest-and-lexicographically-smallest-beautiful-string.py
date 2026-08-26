class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        left = 0
        ones = 0
        ans = ""

        for right in range(n):
            if s[right] == '1':
                ones += 1

            # Jab exactly k ones mil jaye
            while ones == k:
                curr = s[left:right + 1]

                # Shorter substring ya same length but lexicographically smaller
                if ans == "" or len(curr) < len(ans) or (len(curr) == len(ans) and curr < ans):
                    ans = curr

                # left se remove karo
                if s[left] == '1':
                    ones -= 1
                left += 1

        return ans