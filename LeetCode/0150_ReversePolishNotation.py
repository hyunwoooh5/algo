class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbols = set(["+", "-", "*", "/"])
        for token in tokens:
            if token in symbols:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a+b)
                elif token == "-":
                    stack.append(a-b)
                elif token == "*":
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
            else:
                stack.append(int(token))

        return stack[-1]
