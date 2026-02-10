class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        self.current_min = 2**31

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.current_min = min(self.current_min, val)
        self.minstack.append(self.current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        if self.minstack:
            self.current_min = self.minstack[-1]
        else:
            self.current_min = 2**31

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.current_min
