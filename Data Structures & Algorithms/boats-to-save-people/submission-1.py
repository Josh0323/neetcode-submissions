class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        counts = [0] * (max(people) + 1)

        for p in people:
            counts[p] += 1
        
        p_i, c_i = 0, 1
        
        while p_i < len(people):
            while counts[c_i] == 0:
                c_i += 1
            people[p_i] = c_i
            counts[c_i] -= 1
            p_i += 1

        l, r = 0, len(people) - 1
        boats = 0
        while l <= r:
            remain = limit - people[r]
            boats += 1
            r -= 1
            if l <= r and remain >= people[l]:
                l += 1
        return boats