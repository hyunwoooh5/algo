# Time limit
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        m = len(wordDict)
        t = max([len(w) for w in wordDict])

        res = []

        def backtrack(l, path):
            if "".join(path) == s:
                res.append("".join(path))
                return
            elif len("".join(path)) > n:
                return

            for w in wordDict:
                path.append(w)
                backtrack(l+len(w), path)
                path.pop()

        backtrack(0, [])

        if res:
            return True
        return False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        n = len(s)

        dp = [False]*(n+1)
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[-1]
