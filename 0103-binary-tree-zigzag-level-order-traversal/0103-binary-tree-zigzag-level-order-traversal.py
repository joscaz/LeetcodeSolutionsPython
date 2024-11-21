# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root] if root else [])
        ans = []

        while q:
            q_len = len(q)
            cur_level = []
            for i in range(q_len):
                node = q.popleft()
                cur_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            cur_level = cur_level[::-1] if len(ans) % 2 else cur_level
            ans.append(cur_level)
        return ans
        '''
        q = [9] -> len = 2 -> i = 0 -> node = 20
        cur_level = [3] 
        ans = [[], []]
        left = False
        '''