# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        copy = []
        curr = head
        i, j = 0, 0

        while curr:
            copy.append(curr.val)
            curr = curr.next
            j += 1
        j-=1

        while i <= j:
            if copy[i] != copy[j]:
                return False
            i += 1
            j -= 1
        
        return True