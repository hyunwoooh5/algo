class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        res = []

        for a, b in edges:
            if a in res:
                return a
            if b in res:
                return b

            res.append(a)
            res.append(b)
