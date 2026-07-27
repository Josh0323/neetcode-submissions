class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        
        while columnNumber > 0:
            idx = (columnNumber - 1) % 26
            result += chr(ord('A') + idx)
            columnNumber = (columnNumber - 1) // 26

        return result[::-1]