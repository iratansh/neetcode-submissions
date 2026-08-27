class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # backtracking + trie
        # append all words to the trie
        root = TrieNode()

        for word in words:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.word = word
        
        ROWS, COLS = len(board), len(board[0])
        res = []

        def dfs(r, c, node):
            if (not 0 <= r < ROWS) or (not 0 <= c < COLS):
                return 
            ch = board[r][c]
            if ch not in node.children:
                return 
            
            # iterate through the trie?
            next_node = node.children[ch]
            if next_node.word:
                res.append(next_node.word)
                next_node.word = None

            board[r][c] = "#"  # Mark visited

            # Explore 4 directions
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != "#":
                    dfs(nr, nc, next_node)

            board[r][c] = ch   # Backtrack (restore character)
        

        curr = root
        for r in range(ROWS):
            for c in range(COLS):
                # perform dfs starting from every pos in the matrix
                dfs(r, c, curr)
        
        return res