class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l, r = 0, mountainArr.length() - 1
        cache = {}
        def get(i):
            if i not in cache:
                cache[i] = mountainArr.get(i)
            return cache[i]

        while l < r:
            m = l + (r - l) // 2
            if get(m) < get(m + 1):
                l = m + 1
            else:
                r = m
        
        peak, peak_idx = get(l), l
        if peak == target:
            return peak_idx
        
        l, r = 0, peak_idx - 1
        while l <= r:
            m = l + (r - l) // 2
            mid = get(m)
            if mid == target:
                return m
            elif mid < target:
                l = m + 1
            else:
                r = m - 1
        
        l, r = peak_idx, mountainArr.length() - 1
        while l <= r:
            m = l + (r - l) // 2
            mid = get(m)
            if mid == target:
                return m
            elif mid < target:
                r = m - 1
            else:
                l = m + 1
        return -1 