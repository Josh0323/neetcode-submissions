class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.count = 1
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.prev = self.tail
        self.tail.next = self.head
        self.length = 0
    
    def length(self):
        return self.length
    
    def pop(self, node):
        next_node, prev_node = node.next, node.prev
        prev_node.next = next_node
        next_node.prev = prev_node
        node.prev, node.next = None, None

        self.length -= 1
        return node

    def push_left(self, node):
        next_node = self.tail.next
        next_node.prev = node
        self.tail.next = node
        node.next = next_node
        node.prev = self.tail
        self.length += 1
    
    def pop_right(self):
        if self.length == 0:
            return None
        return self.pop(self.head.prev)



class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_map = {}
        self.freq_map = defaultdict(LinkedList)
        self.min_use_count = float('inf')

    def counter(self, node):
        self.freq_map[node.count].pop(node)
        if self.freq_map[node.count].length == 0 and self.min_use_count == node.count:
            self.min_use_count += 1
        node.count += 1
        self.freq_map[node.count].push_left(node)

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        node = self.node_map[key]
        self.counter(node)
        return node.val
 


    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            node = self.node_map[key]
            node.val = value
            self.counter(node)
            return
        
        if self.capacity == len(self.node_map):
            node = self.freq_map[self.min_use_count].pop_right()
            del self.node_map[node.key]
        node = ListNode(key, value)
        self.min_use_count = 1
        self.node_map[key] = node
        self.freq_map[self.min_use_count].push_left(node)
        
            



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)