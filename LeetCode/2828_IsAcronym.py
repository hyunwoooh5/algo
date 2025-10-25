class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return "".join([c[0] for c in words]) == s
