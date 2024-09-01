# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        aux = head

        length = 0
        while aux:
            aux=aux.next
            length+=1
        middle = length // 2
        for i in range(middle):
            head = head.next
        return head

