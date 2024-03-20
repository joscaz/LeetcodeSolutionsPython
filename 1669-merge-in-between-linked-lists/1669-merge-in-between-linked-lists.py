# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        i = 1

        curr = list1
        curr2 = list2
        node_from = None
        node_to = None
        dummyList = ListNode(0)
        dum = dummyList

        while curr:
            if i == a:
                node_from = curr
            
            if i-1 == b:
                node_to = curr.next
                break

            i += 1
            curr = curr.next
        
        while curr2.next:
            curr2 = curr2.next
        curr2.next = node_to
        
        node_from.next = list2
        
        return list1