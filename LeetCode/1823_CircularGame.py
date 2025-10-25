class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        from collections import deque

        dq = deque(range(1, n+1))

        while len(dq) > 1:
            dq.rotate(-(k-1))
            dq.popleft()

        return dq[0]
