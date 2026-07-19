class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        last = {}

        # Har character ka last index store karo
        for i, ch in enumerate(s):
            last[ch] = i

        seen = set()

        for i, ch in enumerate(s):

            # Agar character already stack me hai
            if ch in seen:
                continue

            # Agar stack ka last character bada hai
            # aur wo baad me dobara mil sakta hai,
            # to usse remove kar do
            while stack and stack[-1] > ch and last[stack[-1]] > i:
                removed = stack.pop()
                seen.remove(removed)

            stack.append(ch)
            seen.add(ch)

        return "".join(stack)