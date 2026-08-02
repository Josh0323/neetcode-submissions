class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        # 1. Find the peak
        l, r = 0, n - 1
        while l < r:
            m = l + (r - l) // 2
            if mountainArr.get(m) < mountainArr.get(m + 1):
                l = m + 1   # ascending here → peak is to the right
            else:
                r = m       # descending or at peak → peak is here or left
        peak = l

        # 2. Search ascending half [0, peak]
        l, r = 0, peak
        while l <= r:
            m = l + (r - l) // 2
            val = mountainArr.get(m)
            if val == target:
                return m
            elif val < target:
                l = m + 1
            else:
                r = m - 1

        # 3. Search descending half [peak+1, n-1]
        l, r = peak + 1, n - 1
        while l <= r:
            m = l + (r - l) // 2
            val = mountainArr.get(m)
            if val == target:
                return m
            elif val > target:      # flipped: array decreases here
                l = m + 1
            else:
                r = m - 1

        return -1