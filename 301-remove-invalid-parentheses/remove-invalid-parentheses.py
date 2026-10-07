from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str):
        def is_valid(string):
            count = 0

            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        queue = deque([s])
        visited = {s}
        result = []

        while queue:
            current = queue.popleft()

            # If valid, this is the minimum-removal level
            if is_valid(current):
                result.append(current)

            # Once we find valid strings, don't remove more characters
            if result:
                continue

            # Generate next level by removing one character
            for i in range(len(current)):
                if current[i] not in "()":
                    continue

                next_string = current[:i] + current[i + 1:]

                if next_string not in visited:
                    visited.add(next_string)
                    queue.append(next_string)

        return result