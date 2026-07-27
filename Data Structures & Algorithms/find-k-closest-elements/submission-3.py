class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k >= len(arr):
            return arr
        
        min_window = 0
        m_l, m_r = 0, len(arr) - 1
        window = 0
        l = 0
        for r in range(len(arr)):
            window += abs(arr[r] - x)
            if r < k:
                min_window = window
                m_l, m_r = l, r
            elif r - l + 1 > k:
                window -= abs(arr[l] - x)
                l += 1
                print(r, min_window, window)
                if window < min_window:
                    min_window = window
                    m_l, m_r = l, r
                elif window == min_window:
                    continue
                else:
                    break

        
        return arr[m_l:m_r + 1]

