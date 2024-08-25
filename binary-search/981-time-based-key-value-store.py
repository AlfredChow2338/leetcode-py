# Ask the question: is the value and timestamp sorted? <- imprtant 
# Runtime: 579 ms, faster than 66.48% of Python3 online submissions for Time Based Key-Value Store.
# Memory Usage: 74.7 MB, less than 16.61% of Python3 online submissions for Time Based Key-Value Store.
class TimeMap:
    def __init__(self):
        self.store = {} # key: string, value: List[value,timestamp ]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res