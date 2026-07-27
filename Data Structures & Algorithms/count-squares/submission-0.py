class CountSquares:

    def __init__(self):
        self.saved = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        x, y = point
        self.saved[(x, y)] += 1
        self.points.append((x, y))

    def count(self, point: List[int]) -> int:
        x, y = point
        result = 0
        for xp, yp in self.points:
            if abs(x - xp) != abs(y - yp) or x == xp or y == yp:
                continue
            result += self.saved[(x, yp)] * self.saved[(xp, y)]

        return result
        

