class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

linkedList = LinkedList()
firstNode = ListNode(1)
secondNode = ListNode(2)
thirdNode = ListNode(3)
fourthNode = ListNode(4)

firstNode.next = secondNode
secondNode.next = thirdNode
thirdNode.next = fourthNode
fourthNode.next = None

linkedList.head = firstNode
while linkedList.head is not None:
    print(linkedList.head.val)
    linkedList.head = linkedList.head.next