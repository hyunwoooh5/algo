class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hash_table = {}
        for s in strs:
            key = [0]*26

            for char in s:
                key[ord(char)-ord('a')] += 1

            key = tuple(key)
            if key in hash_table:
                hash_table[key].append(s)
            else:
                hash_table[key] = [s]

        for r in hash_table.values():
            result.append(r)

        return result


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        hash_table = {}

        for word in strs:
            key = [0]*26
            for char in word:
                key[ord(char)-ord('a')] += 1

            key = tuple(key)

            if key in hash_table:
                hash_table[key].append(word)
            else:
                hash_table[key] = [word]

        for _, value in hash_table.items():
            ans.append(value)

        return ans
