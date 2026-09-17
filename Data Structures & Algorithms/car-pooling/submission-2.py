class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        sec = []
        for num, frm, to in trips:
            sec.append((frm, num))
            sec.append((to, -num))
        
        sec.sort()

        cur_cap = 0
        for loc, num in sec:
            cur_cap += num
            if cur_cap > capacity:
                return False
        
        return True