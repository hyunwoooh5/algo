class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash_table = {}

        for i, char in enumerate(s):
            if char in hash_table:
                hash_table[char][1] = i
            else:
                hash_table[char] = [i, i]

        intervals = [value for key, value in hash_table.items()]

        final = [intervals[0]]

        for c, d in intervals[1:]:
            a, b = final[-1]

            if b <= c:
                final.append([c, d])

            else:
                final[-1][1] = max(b, d)

        return [interval[1]-interval[0]+1 for interval in final]


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash_table = {}

        for i, char in enumerate(s):
            hash_table[char] = i

        ans = []

        size = 0
        end = 0  # farthest index

        for i, c in enumerate(s):
            size += 1
            end = max(end, hash_table[c])

            if i == end:
                ans.append(size)
                size = 0
        return ans


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash_table = {}

        for i, char in enumerate(s):
            if char in hash_table:
                hash_table[char][1] = i
            else:
                hash_table[char] = [i, i]

        intervals = [value for key, value in hash_table.items()]

        ans = [intervals[0]]

        for c, d in intervals[1:]:
            a, b = ans[-1]

            if b <= c:
                ans.append([c, d])
            else:
                ans[-1][1] = max(b, d)

        return [interval[1]-interval[0]+1 for interval in ans]
    