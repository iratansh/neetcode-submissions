class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # have sets for each row and col
        N = len(board)
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        # one-pass add nums to each set and check for dups
        for r in range(N):
            for c in range(N):
                if board[r][c] == ".":
                    continue

                box = (r // 3) * 3 + (c // 3)
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[box]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[box].add(board[r][c])
        return True