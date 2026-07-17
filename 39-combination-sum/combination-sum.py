class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(index, current, total):
            # If sum becomes target, store the combination
            if total == target:
                ans.append(current[:])
                return

            # If sum exceeds target or no more candidates
            if total > target or index == len(candidates):
                return

            # Include current candidate
            current.append(candidates[index])
            backtrack(index, current, total + candidates[index])

            # Backtrack
            current.pop()

            # Exclude current candidate
            backtrack(index + 1, current, total)

        backtrack(0, [], 0)
        return ans