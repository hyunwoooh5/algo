class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        m = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
             "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        l = 'abcdefghijklmnopqrstuvwxyz'

        d = {}

        for i in range(26):
            d[l[i]] = m[i]

        ans = []
        for w in words:
            temp = ""
            for i in w:
                temp += d[i]
            ans.append(temp)

        return len(set(ans))
