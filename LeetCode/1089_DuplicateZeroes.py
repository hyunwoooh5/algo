class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i = 0
        n = len(arr)
        while i != len(arr):
            if arr[i] == 0 and i != len(arr)-1:
                arr[i+2:] = arr[i+1:-1]
                arr[i+1] = 0
                i += 2
            else:
                i += 1
