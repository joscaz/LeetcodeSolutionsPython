# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, target):
            if not root:
                return 0
            path_count = 1 if root.val == target else 0
            path_count += dfs(root.left, target - root.val)
            path_count += dfs(root.right, target - root.val)

            return path_count
        
        if not root:
            return 0
        
        return (dfs(root, targetSum)+
            self.pathSum(root.left, targetSum) +
            self.pathSum(root.right, targetSum))