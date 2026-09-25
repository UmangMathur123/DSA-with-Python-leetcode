class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:

        def combine(a, b):
            result = set()

            for x in a:
                for y in b:
                    result.add(x + y)

            return result

        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                
                if expression[i] == '{':
                    inside, i = parse(i + 1)
                    current = combine(current, inside)

                elif expression[i] == ',':
                    result |= current
                    current = {""}
                    i += 1

                else:
                    current = combine(current, {expression[i]})
                    i += 1

            result |= current

            if i < len(expression) and expression[i] == '}':
                i += 1

            return result, i

        answer, _ = parse(0)

        return sorted(answer)