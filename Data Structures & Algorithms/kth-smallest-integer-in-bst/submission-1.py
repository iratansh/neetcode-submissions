# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal always maintains the order?
        # to optimize space could keep vars instead?
        self.k = k
        self.res = None

        def dfs(node):
            if not node or self.res is not None:
                return
            
            dfs(node.left)
            self.k -= 1
            if self.k == 0:
                self.res = node.val
            dfs(node.right) 

        dfs(root)
        return self.res