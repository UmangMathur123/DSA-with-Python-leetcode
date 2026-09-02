class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)

        # If only one element, it is already either odd or even
        if n == 1:
            return True

        has_odd = False
        has_even = False

        for num in nums1:
            if num % 2 == 0:
                has_even = True
            else:
                has_odd = True

        # If all are odd or all are even
        if not (has_odd and has_even):
            return True

        # Both odd and even exist.
        # We can make all elements even:
        # odd - odd = even
        # even - even = even
        if nums1.count(1) >= 0:
            return True

        return False