class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        ans = nums1[:m] + nums2[:n]
        ans.sort()

        for i in range(len(nums1)):
            nums1[i] = ans[i]
