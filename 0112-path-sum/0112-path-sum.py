# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.ans = False
        if not root:
            return self.ans
        
        def dfs(root, cur_sum):
            cur_sum += root.val
            if not root.left and not root.right and cur_sum == targetSum:
                self.ans = True
            if root.left:
                dfs(root.left, cur_sum)
            if root.right:
                dfs(root.right, cur_sum)
        
        dfs(root, 0)
        return self.ans