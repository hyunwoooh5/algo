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


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hash_table = {}

        for task in tasks:
            if task in hash_table:
                hash_table[task] += 1
            else:
                hash_table[task] = 1

        ans = 0

        freqs = [-value for key, value in hash_table.items()]
        heapq.heapify(freqs)

        q = deque()  # (remaining_count, next_available_time)

        while freqs or q:
            ans += 1

            if not freqs:
                ans = q[0][1]

            else:
                cnt = 1 + heapq.heappop(freqs)
                if cnt:
                    q.append([cnt, ans+n])

            if q and q[0][1] == ans:
                heapq.heappush(freqs, q.popleft()[0])

        return ans
