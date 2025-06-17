class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        ans = []
        for i in words:
            l = i.lower()
            if l[0] in keyboard[0]:
                temp = [j in keyboard[0] for j in l[1:]]
                if all(temp):
                    ans.append(i)
            elif l[0] in keyboard[1]:
                temp = [j in keyboard[1] for j in l[1:]]
                if all(temp):
                    ans.append(i)
            else:
                temp = [j in keyboard[2] for j in l[1:]]
                if all(temp):
                    ans.append(i)
        return ans
