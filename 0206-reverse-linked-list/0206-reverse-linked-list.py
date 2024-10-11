# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        # create prev
        # set curr.next to prev
        # create reference to curr.next before changing cur.next ptr
        # assign cur to prev
        # set curr to curr.next

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        return prev