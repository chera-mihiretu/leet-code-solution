# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        remain = length % k
        exist = length // k
        current = head
        answer = []
        while current:
            exist = length // k
            prev = start = end = current
            while exist:
                exist -= 1
                prev = current
                current= current.next
            if remain:
                remain -= 1
                prev = current
                current = current.next
            prev.next = None                
            answer.append(start)
        if len(answer) != k:
            answer.extend([None for i in range(k-len(answer))])
        return answer
            
            
