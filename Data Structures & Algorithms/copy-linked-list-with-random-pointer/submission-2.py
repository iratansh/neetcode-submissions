"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        o_to_c = {}

        def dfs(node):
            if node is None:
                return None
            if node in o_to_c:
                return o_to_c[node]
            
            copy = Node(node.val)
            o_to_c[node] = copy
            copy.next = dfs(node.next)
            copy.random = dfs(node.random)
            return copy

        return dfs(head)
        
