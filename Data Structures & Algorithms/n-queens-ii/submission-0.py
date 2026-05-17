class Solution:
    def totalNQueens(self, n: int) -> int:
        output = 0

        trackVert = set()
        trackDiagP = set()
        trackDiagN = set()

        def backtrack(y):
            nonlocal trackVert
            nonlocal trackDiagP
            nonlocal trackDiagN
            nonlocal n
            nonlocal output
            if y == n:
                output += 1
                return

            for x in range(n):
                if x in trackVert or (x + y) in trackDiagN or (y - x) in trackDiagP:
                    continue

                trackVert.add(x)
                trackDiagP.add(y - x)
                trackDiagN.add(y + x)

                backtrack(y + 1)

                trackVert.remove(x)
                trackDiagP.remove(y - x)
                trackDiagN.remove(y + x)

        backtrack(0)
        return output
            

            