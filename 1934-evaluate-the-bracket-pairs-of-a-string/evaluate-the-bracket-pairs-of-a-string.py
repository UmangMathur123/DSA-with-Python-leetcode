class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        # Knowledge ko dictionary mein convert karo
        mp = {}

        for key, value in knowledge:
            mp[key] = value

        ans = []
        i = 0

        while i < len(s):
            if s[i] == '(':
                # ')' tak key find karo
                j = i + 1

                while s[j] != ')':
                    j += 1

                key = s[i + 1:j]

                # Key known hai to value, warna '?'
                ans.append(mp.get(key, "?"))

                i = j + 1
            else:
                ans.append(s[i])
                i += 1

        return "".join(ans)