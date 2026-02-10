class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == ')':
                if stack:
                    p = stack.pop()
                    if p != '(':
                        return False
                else:
                    return False
            elif char == '}':
                if stack:
                    p = stack.pop()
                    if p != '{':
                        return False
                else:
                    return False
            elif char == ']':
                if stack:
                    p = stack.pop()
                    if p != '[':
                        return False
                else:
                    return False
            else:
                stack.append(char)

        return not stack
