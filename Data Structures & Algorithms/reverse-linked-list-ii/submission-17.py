# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse_list(node, n):
            if n == 1:
                return node, node.next
            
            new_node, next_node = reverse_list(node.next, n - 1)
            node.next.next = node
            node.next = next_node
            return new_node, next_node
        
        if left == 1:
            new_node, _ = reverse_list(head, right)
            return new_node
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head