class Solution:
    def checkValidString(self, s: str) -> bool:
        stack_p = []

        stack_star = []

        for i, char in enumerate(s):
            if char == "(":
                stack_p.append(i)
            elif char == "*":
                stack_star.append(i)

            else:
                if stack_p:
                    stack_p.pop()
                else:
                    if stack_star:
                        stack_star.pop()
                    else:
                        return False

        while stack_p and stack_star:
            if stack_p[-1] > stack_star[-1]:
                return False
            stack_p.pop()
            stack_star.pop()

        return not stack_p


class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open, max_open = 0, 0

        for char in s:
            if char == "(":
                min_open, max_open = min_open+1, max_open + 1
            elif char == ")":
                min_open, max_open = min_open-1, max_open - 1
            else:
                min_open, max_open = min_open-1, max_open + 1

            if max_open < 0:
                return False
            if min_open < 0:
                min_open = 0
        return min_open == 0
