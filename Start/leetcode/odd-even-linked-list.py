# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd_end =  head
        even_start = even_end = head.next
        
        while even_end and even_end.next:
            odd_end.next = even_end.next
            odd_end = odd_end.next
            even_end.next = odd_end.next
            even_end = even_end.next
        odd_end.next = even_start
        return head

                
                


        