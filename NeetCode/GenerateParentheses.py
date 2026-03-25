class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(path, count):
            if count[0] == n and count[1] == n:
                res.append(path)
                return

            if count[0] < n:
                path += "("
                count[0] += 1
                backtrack(path, count)
                path = path[:-1]
                count[0] -= 1

            if count[1] < n and count[0] > count[1]:
                path += ")"
                count[1] += 1
                backtrack(path, count)
                path = path[:-1]
                count[1] -= 1

        backtrack("", [0, 0])

        return res


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(path, count):
            if count[0] == n and count[1] == n:
                res.append("".join(path))
                return

            if count[0] < n:
                path.append("(")
                count[0] += 1
                backtrack(path, count)
                path.pop()
                count[0] -= 1

            if count[1] < n and count[0] > count[1]:
                path.append(")")
                count[1] += 1
                backtrack(path, count)
                path.pop()
                count[1] -= 1

        backtrack([], [0, 0])

        return res


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(op, cl, path):
            if op < cl:
                return
            if op > n or cl > n:
                return
            if op == n and cl == n:
                ans.append("".join(path))
                return

            path.append("(")
            backtrack(op+1, cl, path)
            path.pop()

            path.append(")")
            backtrack(op, cl+1, path)
            path.pop()

        backtrack(0, 0, [])

        return ans
