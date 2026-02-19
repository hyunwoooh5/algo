class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)

        if n > m:
            nums1, nums2 = nums2, nums1
            n, m = m, n

        left, right = 0, n

        while left <= right:
            i = left + (right-left)//2
            j = (m+n+1)//2 - i

            Aleft = nums1[i-1] if i > 0 else float("-inf")
            Aright = nums1[i] if i < n else float("inf")
            Bleft = nums2[j-1] if j > 0 else float("-inf")
            Bright = nums2[j] if j < m else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if (n+m) % 2 == 1:
                    return max(Aleft, Bleft)
                return (max(Aleft, Bleft) + min(Aright, Bright))/2.0
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1
