class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = defaultdict(set)
        col_sets = defaultdict(set)
        box_sets = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                box_ind = (r // 3, c // 3)
                if board[r][c] in row_sets[r] \
                or board[r][c] in col_sets[c] \
                or board[r][c] in box_sets[box_ind]:
                    return False
                row_sets[r].add(board[r][c])
                col_sets[c].add(board[r][c])
                box_sets[box_ind].add(board[r][c])

        return True

