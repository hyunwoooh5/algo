class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        ans = 0
        for o in operations:
            if '-' in o:
                ans -= 1
            elif '+' in o:
                ans += 1
        return ans
