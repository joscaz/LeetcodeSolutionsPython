# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hm = {}
        i = 0
        curr = head

        while curr:
            if curr in hm:
                return curr
            hm[curr] = i
            i += 1
            curr = curr.next
        
        return None