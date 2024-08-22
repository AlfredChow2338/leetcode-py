# Sorting
# Runtime: 144 ms, faster than 11.89% of Python3 online submissions for Min Stack.
# Memory Usage: 20.6 MB, less than 44.55% of Python3 online submissions for Min Stack.
class MinStack:
    def __init__(self):
        self.s = []
        self.minS = []

    def push(self, val: int) -> None:
        self.s.append(val)
        self.minS.append(val)
        self.minS.sort()

    def pop(self) -> None:
        v = self.s.pop()
        self.minS.remove(v)

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.minS[0]

# Min Stack
# Runtime: 50 ms, faster than 81.15% of Python3 online submissions for Min Stack.
# Memory Usage: 20.6 MB, less than 44.55% of Python3 online submissions for Min Stack.
class MinStack:
    def __init__(self):
        self.s = []
        self.minS = []

    def push(self, val: int) -> None:
        self.s.append(val)
        minVal = min(val, self.minS[-1] if self.minS else val)
        self.minS.append(minVal)

    def pop(self) -> None:
        self.s.pop()
        self.minS.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.minS[-1]