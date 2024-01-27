# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        c_next = head.next
        if c_next == None:
            return head
        prev = None
        while current:
            c_next = current.next
            current.next = prev
            prev = current
            current = c_next

            insert = prev
            mover = prev
            incase = None
            
            while mover.next:
                if mover.next.val > insert.val:
                    mover = mover.next
                else:
                    hold = mover.next
                    mover.next = insert
                    incase = insert.next
                    insert.next = hold
                    break
            else:
                if mover != insert:
                    mover.next = insert
                    incase = insert.next
                    insert.next = None
            
            if incase:
                prev = incase

            
        prev , current= None, prev
        while current:
            c_next = current.next
            current.next = prev
            prev = current
            current = c_next
        
            
        return prev
