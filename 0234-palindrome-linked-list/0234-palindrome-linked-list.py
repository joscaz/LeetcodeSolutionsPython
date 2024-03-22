# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lista = []
        curr = head
        i, j = 0, 0

        while curr:
            lista.append(curr.val)
            curr = curr.next
            j+=1

        j -= 1
        
        while i<=j:
            if lista[i] != lista[j]:
                return False
            i += 1
            j -= 1
        return True