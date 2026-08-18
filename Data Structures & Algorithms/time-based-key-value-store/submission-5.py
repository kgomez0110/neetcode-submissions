class TimeMap:
    """
    1, 2, 3, 4, 5
    """
    def __init__(self):
        self.map = {}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [(value, timestamp)]
            return
        insertIndex = self.findInsertIndex(self.map[key], timestamp)
        self.map[key].insert(insertIndex, (value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        if self.map[key][0][1] > timestamp:
            return ""
        # print(self.map[key])
        return self.map[key][self.findInsertIndex(self.map[key], timestamp) - 1][0]

# [1, 4] timestamp 5
# [1] timestamp 4
# [1, 3] timestamp 3
    @staticmethod
    def findInsertIndex(values: list, timestamp: int) -> int:
        low, high = 0, len(values) - 1
        while low <= high:
            mid = (high + low) // 2
            if values[mid][1] <= timestamp:
                low = mid + 1
            else:
                high = mid - 1
        return low
        
