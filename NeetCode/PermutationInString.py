class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)

        if l1 > l2:
            return False

        count_s1 = {}

        for char in s1:
            if char in count_s1:
                count_s1[char] += 1
            else:
                count_s1[char] = 1

        count_s2 = {}
        for i in range(l1):
            if s2[i] in count_s2:
                count_s2[s2[i]] += 1
            else:
                count_s2[s2[i]] = 1

        if count_s1 == count_s2:
            return True

        for i in range(l1, l2):
            new_char = s2[i]
            old_char = s2[i-l1]

            if new_char in count_s2:
                count_s2[new_char] += 1
            else:
                count_s2[new_char] = 1

            count_s2[old_char] -= 1

            if count_s2[old_char] == 0:
                del count_s2[old_char]

            if count_s1 == count_s2:
                return True
        return False
