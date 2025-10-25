class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        n = len(words)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                if words[i] == words[j][::-1]:
                    ans += 1

        return ans


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        d = {}
        ans = 0

        for word in words:
            if (word in d) or (word[::-1] in d):
                try:
                    d[word] += 1
                except:
                    d[word[::-1]] += 1
            else:
                d[word] = 1

        return sum(d.values()) - len(d)
