class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        index = [0]
        stack = []
        for ind, i in enumerate(s):
            if i == '(':
                stack.append('(')
            else:
                stack.pop()
                if stack == []:
                    index.append(ind+1)

        ans = []
        for j in range(len(index)-1):
            ans.append(s[index[j]+1:index[j+1]-1])

        return "".join(ans)
