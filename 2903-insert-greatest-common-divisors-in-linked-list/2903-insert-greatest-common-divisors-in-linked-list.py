# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        curr = head

        while curr.next and curr:
            new = ListNode()
            val_to_insert = gcd(curr.val, curr.next.val)
            new.val = val_to_insert
            temp = curr.next
            curr.next = new
            new.next = temp
            curr = temp
        return head