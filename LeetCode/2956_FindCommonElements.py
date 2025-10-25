class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a1, a2 = 0, 0
        for i in nums1:
            if i in nums2:
                a1 += 1
        for j in nums2:
            if j in nums1:
                a2 += 1
        return [a1, a2]
