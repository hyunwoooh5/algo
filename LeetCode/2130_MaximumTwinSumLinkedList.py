# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow

        while curr:
            next_node = curr.next

            curr.next = prev

            prev = curr
            curr = next_node

        res = float("-inf")

        while head and prev:
            res = max(res, head.val + prev.val)
            head = head.next
            prev = prev.next
        return res
