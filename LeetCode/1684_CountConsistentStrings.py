class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        ans = 0
        for i in words:
            count = 0
            for w in allowed:
                count += i.count(w)
            if count == len(i):
                ans += 1
        return ans
