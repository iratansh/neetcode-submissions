"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # divide and conquer: can naturally recursively split the grid and build nodes 
        # need to find the 4 nodes that make up a quadtree? # how to know if a node is going to be a leaf while still constructing the tree during dfs?

        N = len(grid)
        
        def dfs(r, c, size):
            if size == 1:
                # single cell is a leaf
                return Node(grid[r][c] == 1, True, None, None, None, None)

            half = size // 2
            topLeft = dfs(r, c, half)
            topRight = dfs(r, c + half, half)
            bottomLeft = dfs(r + half, c, half)
            bottomRight = dfs(r + half, c + half, half)

            # merge check: if all 4 are leaves and have the same value then merge into one
            if (topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and
                topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
                return Node(topLeft.val, True, None, None, None, None)

            # return an internal parent node not a leaf
            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)

        return dfs(0, 0, N)