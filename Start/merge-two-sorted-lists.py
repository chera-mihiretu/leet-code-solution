# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode], answer=None)->Optional[ListNode]:
        if list1 != None and list2 != None:
            if list1.val < list2.val:
                if answer == None:
                    answer = list1
                    self.mergeTwoLists(list1.next, list2, answer)
                else:
                    answer.next = list1
                    self.mergeTwoLists(list1.next, list2, answer.next)
            else:
                if answer == None:
                    answer = list2     
                    self.mergeTwoLists(list1, list2.next, answer)
                else:
                    answer.next = list2
                    self.mergeTwoLists(list1, list2.next, answer.next)
                
        elif list1 ==None:
            if answer == None:
                answer = list2
            else:
                answer.next = list2
        elif list2 == None:
            if answer == None:
                answer = list1
            else:
                answer.next = list1
        return answer