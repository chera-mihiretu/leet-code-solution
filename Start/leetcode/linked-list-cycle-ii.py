# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        _hash = set()
        while head:
            if head in _hash:
                return head
            else:

                _hash.add(head)
            head = head.next
            