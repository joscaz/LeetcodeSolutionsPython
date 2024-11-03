# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        even = ListNode()

        flag = False # flag to track odd - even
        cur = head
        odd_ptr = odd
        even_ptr = even

        while cur:
            if flag:
                even_ptr.next = cur
                even_ptr = even_ptr.next
            else:
                odd_ptr.next = cur
                odd_ptr = odd_ptr.next
            cur = cur.next
            flag = not flag

        even_ptr.next = None 
        odd_ptr.next = even.next

        return odd.next