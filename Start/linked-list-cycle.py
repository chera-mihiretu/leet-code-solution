# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        if head.val == float('inf'):
            return True
        head.val = float('inf')
        if head.next != None:
            return self.hasCycle(head.next)
        return False