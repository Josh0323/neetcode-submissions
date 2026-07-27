class MedianFinder:

    def __init__(self):
        self.left, self.right = [], []

    def addNum(self, num: int) -> None:
        if self.right and num > self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush_max(self.left, num)
        
        if len(self.left) > len(self.right) + 1:
            n = heapq.heappop_max(self.left)
            heapq.heappush(self.right, n)
        elif len(self.right) > len(self.left) + 1:
            n = heapq.heappop(self.right)
            heapq.heappush_max(self.left, n)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return self.left[0]
        if len(self.right) > len(self.left):
            return self.right[0]
        return (self.left[0] + self.right[0]) / 2
        