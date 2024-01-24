# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        li = []
        curr = head
        while curr != None:
            li.append(curr.val)
            curr = curr.next
        for i in range(len(li)//2):
            if li[i] != li[len(li)-i-1]:
                return False
        return True
            