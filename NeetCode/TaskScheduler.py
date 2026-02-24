class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        l = len(tasks)
        hash_table = {}

        for task in tasks:
            if task in hash_table:
                hash_table[task] += 1
            else:
                hash_table[task] = 1

        freqs = sorted(hash_table.values(), reverse=True)

        k = 1
        for f in freqs[1:]:
            if f == freqs[0]:
                k += 1
            else:
                break

        return max(l, (freqs[0]-1)*(n+1) + k)
