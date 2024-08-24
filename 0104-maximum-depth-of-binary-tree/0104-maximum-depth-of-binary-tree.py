# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxd(root, depth):
            if root is None:
                return depth
            
            return max(maxd(root.left, depth + 1), maxd(root.right, depth+1))
        
        return maxd(root, 0)
