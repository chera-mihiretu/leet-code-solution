# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode], prev=None) -> Optional[ListNode]:
        if head != None:
            hold = head.next
            head.next = prev
            if hold== None:
                return head
            return self.reverseList(hold, head)
        return head
        
        