class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = [i for i in s]
        t = [j for j in t]
        s.sort()
        t.sort()
        return s == t


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s, dict_t = {}, {}

        for char in s:
            if char in dict_s:
                dict_s[char] += 1
            else:
                dict_s[char] = 0

        for char in t:
            if char in dict_t:
                dict_t[char] += 1
            else:
                dict_t[char] = 0

        for char in dict_s:
            if char in dict_t:
                if dict_s[char] != dict_t[char]:
                    return False
            else:
                return False

        for char in dict_t:
            if char in dict_s:
                if dict_s[char] != dict_t[char]:
                    return False
            else:
                return False

        return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}

        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1

        return sum(count.values()) == 0
