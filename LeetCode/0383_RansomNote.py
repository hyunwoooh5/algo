import collections


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counts = collections.Counter(magazine)

        for i in ransomNote:
            if counts[i] > 0:
                counts[i] -= 1
            elif counts[i] == 0:
                return False
        return True
