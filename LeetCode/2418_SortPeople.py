class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        s = [a for b, a in sorted(zip(heights, names), reverse=True)]

        return s
