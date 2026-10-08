class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        balance = 0

        for ch in s:
            if ch == '(':
                # Agar balance 0 hai, ye outermost '(' hai
                if balance > 0:
                    result.append(ch)
                balance += 1

            else:
                balance -= 1

                # Agar balance 0 ho gaya, ye outermost ')' hai
                if balance > 0:
                    result.append(ch)

        return ''.join(result)