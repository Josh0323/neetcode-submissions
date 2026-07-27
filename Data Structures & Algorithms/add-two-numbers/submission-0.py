# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = second = 0

        curr = l1
        ind = 0
        while curr:
            first += curr.val * (10 ** ind) 
            curr = curr.next
            ind += 1
        
        curr = l2
        ind = 0
        while curr:
            second += curr.val * (10 ** ind)
            curr = curr.next
            ind += 1
        
        result = first + second

        dummy = curr = ListNode()
        while result > 0:
            curr.val = result % 10
            result = result // 10
            if result > 0:
                curr.next = ListNode()
                curr = curr.next
        return dummy