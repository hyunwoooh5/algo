class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        k = 0
        for i in range(1, n+1):
            if i in target:
                k = i

        for i in range(1, k+1):
            if i not in target:
                ans.append('Push')
                ans.append('Pop')
            else:
                ans.append('Push')

        return ans
