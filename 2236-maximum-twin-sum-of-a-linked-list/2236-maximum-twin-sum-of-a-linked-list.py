# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reversing list starting from slow 
        cur = slow
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        print(prev)
        
        # list is reversed now, head of rev list is prev
        # start doing the twin sum
        max_sum = 0
        ptr1 = head
        ptr2 = prev

        # both half should have same length
        while ptr1 and ptr2:
            cur_sum = ptr1.val + ptr2.val
            ptr1, ptr2 = ptr1.next, ptr2.next
            max_sum = max(max_sum, cur_sum)
        
        return max_sum