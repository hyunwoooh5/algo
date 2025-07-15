class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        ans = []

        for i in logs:
            if i == "./":
                pass
            elif i == "../":
                if len(ans) != 0:
                    ans.pop()
            else:
                ans.append(i)
            print(ans)

        return len(ans)
