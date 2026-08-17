# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        q = deque([root])
        res = []

        while q:
            q_len = len(q)
            level = []

            for _ in range(q_len):
                n = q.popleft()
                level.append(n.val)

                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            res.append(level)
        return res