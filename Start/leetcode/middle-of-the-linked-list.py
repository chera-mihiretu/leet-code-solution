# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode], num_mid=[-1,-2]) -> Optional[ListNode]:
        slow = fast = head
        while fast:
            if fast.next == None:
                return slow
            slow = slow.next
            fast = fast.next.next
        return slow