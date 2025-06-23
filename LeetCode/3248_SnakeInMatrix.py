class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        """
        :type n: int
        :type commands: List[str]
        :rtype: int
        """
        x, y = 0, 0
        for c in commands:
            if c == "RIGHT":
                x += 1
            elif c == "LEFT":
                x -= 1
            elif c == "DOWN":
                y += 1
            elif c == "UP":
                y -= 1
        return x + n*y
