# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        
        from math import gcd

        while cur.next:
            n1, n2 = cur.val, cur.next.val
            gcd_node = ListNode(gcd(n1, n2), cur.next)
            cur.next = gcd_node
            cur = cur.next.next
        
        return head