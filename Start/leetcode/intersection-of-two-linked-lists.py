# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = []
        b = []
        while headA:
            a.append(headA)
            headA = headA.next
        while headB:
            b.append(headB)
            headB = headB.next
        
        small_len = min(a, b , key=lambda x: len(x))
        index = -1
        for i in range(len(small_len)):
            if a[-(i+1)] == b[-(i+1)]:
                index = i + 1
            else:
                break
        if index >= len(small_len):
            if a == small_len:
                return b[-(i+1)]
            else:
                return a[-(i+1)]
        return None if index == -1 else a[-(i)]