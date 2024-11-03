# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, cur_sum):
            if not root: return 0
            cur_sum += root.val

            path_count = prefix_sum[cur_sum - targetSum]
            prefix_sum[cur_sum] += 1

            path_count += dfs(root.left, cur_sum)
            path_count += dfs(root.right, cur_sum)

            prefix_sum[cur_sum] -= 1

            return path_count
        
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        return dfs(root, 0)