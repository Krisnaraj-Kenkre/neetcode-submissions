class LinkedList:

    class ListNode:

        def __init__(self, val):
            self.next = None
            self.val = val

    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        if index < 0: return -1
        cur = self.head
        if cur is None:
            return -1
        for i in range(index):
            cur = cur.next
            if cur is None:
                return -1
        return cur.val

    def insertHead(self, val: int) -> None:
        if self.head is None:
            self.head = self.ListNode(val)
            self.head.next = None
            self.tail = self.head
        else:
            tmp = self.head
            self.head = self.ListNode(val)
            self.head.next = tmp


    def insertTail(self, val: int) -> None:
        if self.head is None:
            self.head = self.ListNode(val)
            self.head.next = None
            self.tail = self.head
        else:
            self.tail.next = self.ListNode(val)
            self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        if index < 0: return False

        if self.head is None: return False

        if index == 0:
            if self.tail == self.head:
                self.tail = None
                self.head = None
                return True
            self.head = self.head.next
            return True
        
        cur = self.head

        for i in range(index-1):
            if cur.next is None:
                return False
            cur = cur.next

        if cur.next is None: return False
        if self.tail == cur.next:
            self.tail = cur
        cur.next = cur.next.next
        return True



    def getValues(self) -> List[int]:
        arr = []
        if self.head is None: return arr
        cur = self.head
        while cur is not None:
            arr.append(cur.val)
            cur = cur.next
        return arr
        
