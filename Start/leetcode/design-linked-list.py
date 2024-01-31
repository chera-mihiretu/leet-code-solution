class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
class MyLinkedList:
    def __init__(self):
        self.dummy = Node()
        self.tail = self.dummy
        self.size = 0
    def get(self, index: int) -> int:
        temp = self.dummy
        if self.size > index:
            for i in range(index+1):
                temp = temp.next
            return temp.val
        return -1

    def addAtHead(self, val: int) -> None:
        self.dummy.next = Node(val, self.dummy.next)
        if not self.dummy.next.next:
            self.tail = self.dummy.next
        self.size += 1
    def addAtTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next
        self.size += 1
    def addAtIndex(self, index: int, val: int) -> None:
        temp = self.dummy
        if self.size > index:
            for i in range(index):
                temp = temp.next
            temp.next = Node(val, temp.next)
            self.size += 1
        elif self.size == index:
            self.addAtTail(val)
        
    def deleteAtIndex(self, index: int) -> None:
        temp = self.dummy
        prev = self.dummy
        if self.size > index:
            for i in range(index+1):
                prev = temp
                temp = temp.next
            if not temp.next:
                self.tail = prev
                prev.next = None
            else:
                prev.next = temp.next
            self.size -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)