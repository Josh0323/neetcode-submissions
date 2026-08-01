class FreqStack:

    def __init__(self):
        self.count = defaultdict(int)
        self.stacks = [[]]

    def push(self, val: int) -> None:
        self.count[val] += 1
        if self.count[val] == len(self.stacks):
            self.stacks.append([])
        self.stacks[self.count[val]].append(val)

    def pop(self) -> int:
        val = self.stacks[-1].pop()
        self.count[val] -= 1
        if not self.stacks[-1]:
            self.stacks.pop()
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()