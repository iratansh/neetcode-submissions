# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pre_idx = 0
        in_map = {val: i for i, val in enumerate(inorder)}

        def dfs(l, r):
            if l > r:
                return 
            
            val = preorder[self.pre_idx]
            self.pre_idx += 1

            root = TreeNode(val)
            root.left = dfs(l, in_map[val] - 1)
            root.right = dfs(in_map[val] + 1, r)
            return root

        return dfs(0, len(inorder) - 1)
