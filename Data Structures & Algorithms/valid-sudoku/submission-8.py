class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validColumn(board, i):
            track = {}

            for j in range(9):
                if board[i][j] !="." and board[i][j] in track:
                    return False

                track[board[i][j]] = True

            return True

        def validRow(board, j):
            track = {}

            for i in range(9):
                if board[i][j] !="." and board[i][j] in track:
                    return False

                track[board[i][j]] = True

            return True

        def validSquare(board, off):
            track = {}

            i_off = off % 3 * 3
            j_off = off // 3 * 3

            for i_add in range(3):
                for j_add in range(3):
                    i = i_add + i_off
                    j = j_add + j_off

                    if board[i][j] !="." and board[i][j] in track:
                        return False

                    track[board[i][j]] = True

            return True

        for i in range(9):
            if not validColumn(board, i):
                return False

            if not validRow(board, i):
                return False

            if not validSquare(board, i):
                return False

        return True

            