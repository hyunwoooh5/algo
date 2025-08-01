class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        count = 0
        repeated_word = word

        while repeated_word in sequence:
            count += 1
            repeated_word += word

        return count
