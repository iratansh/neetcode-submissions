class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.P = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        # init the prefix matrix
        for r in range(ROWS):
            for c in range(COLS):
                self.P[r + 1][c + 1] = (
                    self.P[r][c + 1] 
                    + self.P[r + 1][c] 
                    - self.P[r][c] 
                    + matrix[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # so the bounds of the inner matrix are restricted by
        # the invisible border of (r1, c1) and (r2, c2)
        # the naive approach is to do a iterative loop using those bounds on self.matrix and sum the values but that's O(N)
        # we can have the matrix as a list since we aren't iterating through the list and instead are just doing indexed lookups it should be O(1)
        # Can compute the res using this formula:
        # P[r2][c2] - P[r1 - 1][c2] - P[r2][c1 - 1] + P[r1 - 1][c1 - 1]
        row1, row2, col1, col2 = row1 + 1, row2 + 1, col1 + 1, col2 + 1
        return (
            self.P[row2][col2] 
            - self.P[row1 - 1][col2] 
            - self.P[row2][col1 - 1] 
            + self.P[row1 - 1][col1 - 1]
        )




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)