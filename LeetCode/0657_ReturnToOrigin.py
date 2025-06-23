class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        l = [0, 0]
        for m in moves:
            if m == 'U':
                l[1] += 1
            elif m == 'D':
                l[1] -= 1
            elif m == 'R':
                l[0] += 1
            elif m == 'L':
                l[0] -= 1
        if l == [0, 0]:
            return True
        return False
