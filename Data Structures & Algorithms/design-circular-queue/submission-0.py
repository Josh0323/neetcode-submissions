class ListNode:
    def __init__(self, val, nxt, prev):
        self.val = val
        self.next = nxt
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = ListNode(0, None, None)
        self.tail = ListNode(0, self.head, None)
        self.head.prev = self.tail
        self.k = k
        self.length = 0

    def enQueue(self, value: int) -> bool:
        if self.length + 1 > self.k:
            return False
        next_node = self.tail.next
        new_node = ListNode(value, next_node, self.tail)
        next_node.prev = new_node
        self.tail.next = new_node
        self.length += 1
        return True

    def deQueue(self) -> bool:
        if self.length == 0:
            return False
        del_node = self.head.prev
        prev_node = del_node.prev
        self.head.prev = prev_node
        prev_node.next = self.head
        del_node.next = None
        del_node.prev = None
        self.length -= 1
        return True
    

    def Front(self) -> int:
        if self.length == 0:
            return -1
        return self.head.prev.val

    def Rear(self) -> int:
        if self.length == 0:
            return -1
        return self.tail.next.val

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()