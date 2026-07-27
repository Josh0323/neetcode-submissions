class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in row_sets[r]:
                    return False
                row_sets[r].add(board[r][c])

                if board[r][c] in col_sets[c]:
                    return False
                col_sets[c].add(board[r][c])

                box_ind = c // 3 + (r // 3) * 3
                if board[r][c] in box_sets[box_ind]:
                    return False
                box_sets[box_ind].add(board[r][c])

        return True

