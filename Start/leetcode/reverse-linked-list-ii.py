# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        slow = start = fast = head
        if right == left:
            return head
        for i in range(right):
            fast = fast.next
        for i in range(left-1):
            start = start.next
            if i != 0:
                slow = slow.next
        #reversing inside link
        prev = fast
        times = right - left + 1
        while times > 0:
            hold = start.next
            start.next = prev
            prev = start
            times -= 1
            if times  <= 0:
                if left != 1:
                    slow.next = start
                else:
                    head = start
                continue
            start = hold
            
        
        return head


        


        