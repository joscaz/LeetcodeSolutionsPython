# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        level = 1
        max_sum = float("-inf") # there may be nodes with value < 0
        min_level = 1

        while q:
            cur_sum = 0
            for i in range(len(q)):
                node = q.popleft()
                cur_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            if cur_sum > max_sum:
                max_sum = cur_sum
                min_level = level
            level += 1
        return min_level