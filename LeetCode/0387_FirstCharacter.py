import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}

        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        print(d)
        for key in d:
            if d[key] == 1:
                count = 0
                for i in range(len(s)):
                    if s[i] == key:
                        return count
                    count += 1
        return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        Given a string s, find the first non-repeating character in it and return its index.
        If it does not exist, return -1.
        """
        count = collections.Counter(s)

        for i, char in enumerate(s):
            print(i, char)
            if count[char] == 1:
                return i

        return -1
