class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = "+-*/"

        for token in tokens:
            if token not in op:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a+b)
                elif token == "-":
                    stack.append(a-b)
                elif token == "*":
                    stack.append(a*b)
                elif token == "/":
                    stack.append(int(a/b))

        return stack[-1]
