# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        
        sublist_head = prev.next
        sublist_tail = sublist_head

        for _ in range(right - left):
            sublist_tail = sublist_tail.next
        after_tail = sublist_tail.next
        sublist_tail.next = None

        reversed_sublist = self.reverse_sublist(sublist_head)
        prev.next = reversed_sublist
        sublist_head.next = after_tail

        return dummy.next

    def reverse_sublist(self, head):
        if not head:
            return None
        new_head = head
        if head.next:
            new_head = self.reverse_sublist(head.next)
            head.next.next = head
        head.next = None
        return new_head