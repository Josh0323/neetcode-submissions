class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ru, rd = 0, len(matrix) - 1

        while ru <= rd:
            m = ru + (rd - ru) // 2

            if matrix[m][0] > target:
                rd = m - 1
            elif matrix[m][-1] < target:
                ru = m + 1
            else:
                break
        
        if ru > rd:
            return False
        
        ru = m

        l, r = 0, len(matrix[ru]) - 1

        while l <= r:
            m = l + (r - l) // 2
            if matrix[ru][m] > target:
                r = m - 1
            elif matrix[ru][m] < target:
                l = m + 1
            else:
                return True
        return False
        
