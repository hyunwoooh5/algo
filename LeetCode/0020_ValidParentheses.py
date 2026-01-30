class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return False
                elif stack[-1] != '(':
                    return False
                stack.pop()
            elif char == '{':
                stack.append(char)
            elif char == '}':
                if not stack:
                    return False
                elif stack[-1] != '{':
                    return False
                stack.pop()
            elif char == '[':
                stack.append(char)
            elif char == ']':
                if not stack:
                    return False
                elif stack[-1] != '[':
                    return False
                stack.pop()
        print(stack)
        return not stack


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # A dictionary to map opening brackets to their corresponding closing brackets
        bracket_map = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        for char in s:
            if char in bracket_map:  # It's an opening bracket
                stack.append(bracket_map[char])
            else:  # It's a closing bracket
                if not stack:  # No opening bracket to match
                    return False
                if stack.pop() != char:  # Mismatch
                    return False

        # After iterating through the string, the stack should be empty if all brackets are matched
        return not stack


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False

            else:
                stack.append(char)

        return not stack 
