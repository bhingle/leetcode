class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        cols = set()
        posDiag = set() # (row + col)
        negDiag = set() # (row - col)
        solution = []

                  

        def backtrack(row):
            if row == n:
                ans = ["".join(i) for i in matrix]
                solution.append(ans)
                return
            for col in range(n):
                if col in cols or (row + col) in posDiag or (row - col) in negDiag:
                    continue
                cols.add(col)
                posDiag.add(row+col)
                negDiag.add(row-col)
                matrix[row][col] = "Q"

                backtrack(row + 1)

                cols.remove(col)
                posDiag.remove(row+col)
                negDiag.remove(row-col)
                matrix[row][col] = "."
        matrix = [ ["."] * n for i in range(n)]
        backtrack(0)
        return solution
        