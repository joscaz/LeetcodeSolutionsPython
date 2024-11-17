# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0
        def dfs(node, max_val):
            if not node: return 0
            self.good = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)

            self.good += dfs(node.left, max_val)
            self.good += dfs(node.right, max_val)
            return self.good
        
        dfs(root, root.val)
        return self.good