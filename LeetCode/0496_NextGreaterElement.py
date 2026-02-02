class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        stack = []
        hash_table = {}

        for num2 in nums2:
            while stack and num2 > stack[-1]:
                val = stack.pop()
                hash_table[val] = num2

            stack.append(num2)

        for num1 in nums1:
            if num1 in hash_table:
                result.append(hash_table[num1])
            else:
                result.append(-1)

        return result
