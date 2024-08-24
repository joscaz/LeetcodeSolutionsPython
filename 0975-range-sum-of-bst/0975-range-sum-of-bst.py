# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        suma = 0
        def rangeSum(root, low, high):
            nonlocal suma
            if root is None:
                return 
            
            rangeSum(root.left, low, high)
            if root.val >= low and root.val <= high:
                suma += root.val
            rangeSum(root.right, low, high)

        rangeSum(root, low, high)

        return suma