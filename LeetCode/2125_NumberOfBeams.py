class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ones = [c.count("1") for c in bank]
        ones = [i for i in ones if i != 0]
        ans = 0
        for i in range(len(ones)-1):
            ans += ones[i] * ones[i+1]

        return ans
