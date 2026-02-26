class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        s = sum(arr[:k])

        n = len(arr)

        count = 1 if s >= k*threshold else 0

        for i in range(k, n):
            s += arr[i]-arr[i-k]

            count = count + 1 if s >= k*threshold else count

        return count
