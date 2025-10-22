class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        s_dict, t_dict = {}, {}

        for index in range(len(s)):
            s_dict[s[index]] = index
            t_dict[t[index]] = index

        return sum([abs(s_dict[i]-t_dict[i]) for i in s])
