class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(start, path):
            if start >= len(s):
                res.append(list(path))
                return

            for j in range(start, len(s)):
                if self.isPalindrome(s, start, j):
                    path.append(s[start:j+1])
                    backtrack(j + 1, path)
                    path.pop()

        backtrack(0, [])
        return res

    def isPalindrome(self, s, i, j):
        l, r = i, j

        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False

        return True


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        n = len(s)

        def backtrack(start, path):
            if start >= n:
                ans.append(list(path))
                return

            for i in range(start, n):
                if self.isPalindrome(s, start, i):
                    path.append(s[start:i+1])
                    backtrack(i+1, path)
                    path.pop()

        backtrack(0, [])

        return ans

    def isPalindrome(self, s, i, j):
        l, r = i, j

        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False

        return True
