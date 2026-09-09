class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        moves = []
        for num, frm, to in trips:
            moves.append([frm, num])
            moves.append([to, -num])
        
        moves.sort()

        cur = 0
        for loc, num in moves:
            cur += num
            if cur > capacity:
                return False
        
        return True