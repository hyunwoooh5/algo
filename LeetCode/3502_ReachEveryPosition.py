class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        ans = [cost[0]]

        for i in cost[1:]:
            if ans[-1] < i:
                ans.append(ans[-1])
            else:
                ans.append(i)

        return ans
