class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        diff = [arr[i+1]-arr[i] for i in range(len(arr)-1)]
        m = min(diff)

        return [[arr[i], arr[i+1]] for i in range(len(diff)) if diff[i] == m]
