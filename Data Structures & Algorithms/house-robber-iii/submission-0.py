# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # entrance is root
        # each house has only one parent
        # can't rob 2 directly linked homes
        # return max money that can be stolen
        # tree dp? post order serves as bottom up. For each node either we rob it or do not rob it

        def dfs(node):
            if not node:
                return (0, 0) # [rob_this, skip_this]
            
            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)

            rob_this = node.val + left_skip + right_skip
            skip_this = max(left_rob, left_skip) + max(right_rob, right_skip)
            return (rob_this, skip_this)
        
        return max(dfs(root))
            

        