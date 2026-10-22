
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        drop_inc = 0
        drop_dec = 0

        # Count breaks in increasing and decreasing order
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                drop_inc += 1
            else:
                drop_dec += 1

        # Check whether sorting is impossible
        bad_inc = (
            drop_inc > 1
            or (drop_inc == 1 and nums[-1] > nums[0])
        )

        bad_dec = (
            drop_dec > 1
            or (drop_dec == 1 and nums[-1] < nums[0])
        )

        if bad_inc and bad_dec:
            return -1

        # Already sorted in increasing order
        if drop_inc == 0:
            return 0

        # Reverse once to sort
        if drop_dec == 0:
            return 1

        # Sort using left rotations
        if drop_inc == 1 and nums[-1] < nums[0]:
            for i in range(1, n):
                if nums[i] < nums[i - 1]:
                    return min(i, n - i + 2)

        # Sort using rotations and one reversal
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                return min(i + 1, n - i + 1)

        return -1
