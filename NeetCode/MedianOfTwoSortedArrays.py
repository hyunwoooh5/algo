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


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m, n = len(nums1), len(nums2)

        i, j = 0, 0

        s = []

        while i < m and j < n:
            if nums1[i] > nums2[j]:
                s.append(nums2[j])
                j += 1

            else:
                s.append(nums1[i])
                i += 1

        while i < m:
            s.append(nums1[i])
            i += 1
        while j < n:
            s.append(nums2[j])
            j += 1

        print(s)

        if (m+n) % 2 == 0:
            x = (m+n)//2
            return (s[x-1]+s[x])/2
        else:
            return s[(m+n)//2]


class Solution:
    def get_kth(self, a: List[int], m: int, b: List[int], n: int, k: int, a_start: int = 0, b_start: int = 0) -> int:
        if m > n:
            return self.get_kth(b, n, a, m, k, b_start, a_start)
        if m == 0:
            return b[b_start+k-1]
        if k == 1:
            return min(a[a_start], b[b_start])

        i = min(m, k//2)
        j = min(n, k//2)

        if a[a_start + i - 1] > b[b_start + j - 1]:
            return self.get_kth(a, m, b, n - j, k - j, a_start, b_start + j)
        else:
            return self.get_kth(a, m - i, b, n, k - i, a_start + i, b_start)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left = (len(nums1) + len(nums2) + 1) // 2
        right = (len(nums1) + len(nums2) + 2) // 2
        return (self.get_kth(nums1, len(nums1), nums2, len(nums2), left) +
                self.get_kth(nums1, len(nums1), nums2, len(nums2), right)) / 2.0
