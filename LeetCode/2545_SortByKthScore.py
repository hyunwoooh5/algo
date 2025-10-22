class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(score), len(score[0])
        kth = [score[i][k] for i in range(m)]

        indexed_data = list(enumerate(kth))
        sorted_data = sorted(indexed_data, key=lambda x: x[1], reverse=True)

        return [score[i[0]] for i in sorted_data]
