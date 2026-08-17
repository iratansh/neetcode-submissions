# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # three cases: 
        # curr node is the lca, lca in left subtree, lca in right subtree
        
        def dfs(node):
            if not node:
                return
            if p.val > node.val and q.val > node.val: # lca in right subtree
                return dfs(node.right)
            elif p.val < node.val and q.val < node.val: # lca in left subtree
                return dfs(node.left)
            return node
        
        return dfs(root)