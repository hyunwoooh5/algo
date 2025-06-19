class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return [0]*len(code)
        elif k > 0:
            return [sum((code[i:]+code[:i])[:k]) for i in range(1, len(code)+1)]
        elif k < 0:
            return [sum((code[i:]+code[:i])[k:]) for i in range(len(code))]
