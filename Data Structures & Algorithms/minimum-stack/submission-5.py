class MinStack:
    def __init__(self):
        self.items = []
        self.min = []

    def push(self, val: int) -> None:
        self.items += [val]
        if self.min and val <= self.min[-1]:
            self.min += [val]
        elif not self.min:
            self.min = [val]

    def pop(self) -> None:
        if self.items:
            if self.min[-1] == self.items[-1]:
                del self.min[-1]
            del self.items[-1]

    def top(self) -> int:
        if self.items:
            return self.items[-1]

    def getMin(self) -> int:
        if self.min:
            return self.min[-1]