# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        prev = head
        curr = head.next
        index = 1

        first = -1
        last = -1
        min_dist = float('inf')

        while curr.next:
            # Local maxima or local minima
            if ((curr.val > prev.val and curr.val > curr.next.val) or
                (curr.val < prev.val and curr.val < curr.next.val)):

                # First critical point
                if first == -1:
                    first = index
                else:
                    # Distance from previous critical point
                    min_dist = min(min_dist, index - last)

                # Update last critical point
                last = index

            prev = curr
            curr = curr.next
            index += 1

        # Fewer than 2 critical points
        if first == -1 or first == last:
            return [-1, -1]

        max_dist = last - first

        return [min_dist, max_dist]