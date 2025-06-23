class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        ans = []
        for ind, w in enumerate(words):
            if x in w:
                ans.append(ind)
        return ans
