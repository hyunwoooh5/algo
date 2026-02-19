class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d:
            self.d[key].append([value, timestamp])
        else:
            self.d[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        l = self.d[key]

        left, right = 0, len(l)-1
        res = ""

        while left <= right:
            mid = left + (right-left)//2

            if l[mid][1] > timestamp:
                right = mid - 1
            elif l[mid][1] < timestamp:
                res = l[mid][0]
                left = mid + 1

            else:
                return l[mid][0]

        return res
