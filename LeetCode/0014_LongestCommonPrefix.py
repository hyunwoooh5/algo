from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(len(strs[0])+1):  # Compare with the first element
            for num, j in enumerate(strs):
                if j[:i] != strs[0][:i]:  # different then finish
                    break
                # check if the loop went to the last
                elif j == strs[-1] and num == len(strs)-1:
                    prefix = strs[0][:i]
        return prefix
