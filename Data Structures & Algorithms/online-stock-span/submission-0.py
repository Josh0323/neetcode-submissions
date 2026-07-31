class StockSpanner:

    def __init__(self):
        self.stack, self.can = [], []

    def next(self, price: int) -> int:
        span = 1

        while self.stack:
            if self.stack[-1] <= price:
                self.can.append(self.stack.pop())
                span += 1
            else:
                break
        
        while self.can:
            self.stack.append(self.can.pop())
        
        self.stack.append(price)
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)