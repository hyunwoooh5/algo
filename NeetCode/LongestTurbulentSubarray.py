class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)

        res = 0
        count = 0

        prev = 0

        for i in range(n-1):
            if arr[i] > arr[i+1]:
                count = count + 1 if prev == -1 else 1
                prev = 1
            elif arr[i] < arr[i+1]:
                count = count + 1 if prev == 1 else 1
                prev = -1
            else:
                count = 0
                prev = 0

            res = max(res, count)

        return res + 1
