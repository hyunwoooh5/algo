class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        init, final = 0, 1
        s = [i for i in s]
        while init != final:
            init = len(s)
            for i in range(len(s)-1):
                if s[i] == s[i+1]:
                    s.pop(i)
                    s.pop(i)
                    break
            final = len(s)

        return "".join(s)


class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        init, final = 0, 1

        while init != final:
            stack = []
            init = len(s)
            for i in s:
                if stack == [] or stack[-1] != i:
                    stack.append(i)
                else:
                    stack.pop()
            s = stack
            final = len(s)

        return "".join(s)
