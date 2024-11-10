# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # we can apply slow and fast ptr approach, then reverse from slow
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse 2nd half
        prev = None
        cur = slow
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True 