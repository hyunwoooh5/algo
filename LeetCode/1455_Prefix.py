class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        sentence = sentence.split()
        length = len(searchWord)

        for i in range(len(sentence)):
            if sentence[i][:length] == searchWord:
                return i+1
        return -1
