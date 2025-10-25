class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        n_min = min(n1, n2)

        ans = ""

        for i in range(n_min):
            ans += word1[i] + word2[i]

        if n1 > n2:
            return ans + word1[n_min:]
        elif n1 < n2:
            return ans + word2[n_min:]
        else:
            return ans
