class Solution:
    def countPoints(self, rings: str) -> int:
        d = {}
        n = len(rings)
        for i in range(n//2):
            if int(rings[2*i+1]) in d:
                d[int(rings[2*i+1])] += rings[2*i]
            else:
                d[int(rings[2*i+1])] = rings[2*i]

        ans = 0
        for k in d.values():
            if 'R' in k and 'G' in k and 'B' in k:
                ans += 1
        return ans
