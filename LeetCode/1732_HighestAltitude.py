class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        al = [0]

        for i in gain:
            al.append(al[-1]+i)

        return max(al)
