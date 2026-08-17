# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # for a node to be considered good there must be no nodes along the path with val > X
        self.res = 0
        def dfs(node, max_val):
            if not node:
                return
            
            if node.val >= max_val:
                self.res += 1   
            
            curr_max = max(max_val, node.val)
            dfs(node.left, curr_max)
            dfs(node.right, curr_max)

        dfs(root, float("-inf"))
        return self.res