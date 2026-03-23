class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_table = {}

        for char in s:
            if char in hash_table:
                hash_table[char] += 1
            else:
                hash_table[char] = 1

        for char in t:
            if char in hash_table:
                hash_table[char] -= 1
            else:
                return False

        for key in hash_table:
            if hash_table[key] != 0:
                return False

        return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_table = {}

        for char in s:
            if char in hash_table:
                hash_table[char] += 1
            else:
                hash_table[char] = 1

        for char in t:
            if char in hash_table:
                if hash_table[char] > 0:
                    hash_table[char] -= 1
                else:
                    return False
            else:
                return False

        return True
