class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}

        # Counting
        for s in strs:
            temp = [0]*26
            for char in s:
                temp[ord(char)-ord('a')] += 1

            temp = tuple(temp)

            if temp in hash_table:
                hash_table[temp].append(s)
            else:
                hash_table[temp] = [s]

        return list(hash_table.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}

        # Sorting
        for s in strs:
            key = "".join(sorted(s))

            if key in hash_table:
                hash_table[key].append(s)
            else:
                hash_table[key] = [s]

        return list(hash_table.values())
