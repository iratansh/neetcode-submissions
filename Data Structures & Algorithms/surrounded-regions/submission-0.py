class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # regions can be surrounded as long as its completely enclosed by X's
        # we can run a dfs from every 0 on the border -> mark regions that are reachable from the border 0's and then set those values to # and then do a second pass to updae all 0's to X's and then a third pass to update all #'s to O's
        ROWS, COLS = len(board), len(board[0])

        def dfs(i, j):
            if (not 0 <= i < ROWS) or (not 0 <= j < COLS) or board[i][j] != "O":
                return

            board[i][j] = "#"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
        

