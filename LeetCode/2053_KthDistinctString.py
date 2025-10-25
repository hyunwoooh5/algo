class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        ans = []
        for j in d:
            if d[j] == 1:
                ans.append(j)

        if len(ans) < k:
            return ""
        return ans[k-1]
