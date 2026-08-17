# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 3 cases when node.val == key
        # no children: return None to the parent
        # one child: return whatever child exists
        # two children: find the inorder sucessor

        def dfs(node, target_key):
            if not node:
                return
            
            if target_key < node.val:
                node.left = dfs(node.left, target_key)
            elif target_key > node.val:
                node.right = dfs(node.right, target_key)
            else:
                # case 1
                if not node.left and not node.right:
                    return 
                
                # case 2
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                
                # case 3: the node to be deleted should get replaced by the lowest node in the right subtree
                curr = node.right
                while curr.left:
                    curr = curr.left
                node.val = curr.val
                # recursively delete the now duplicated node from the right subtree
                node.right = dfs(node.right, node.val)
            return node
        return dfs(root, key)