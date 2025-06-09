class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = str(n)
        while True:
            ans = 0
            for i in range(len(n)):
                ans += int(n[i])**2

            n = str(ans)
            # print(n)
            if ans == 1:
                return True
            elif ans == 7 and len(n) == 1:
                return True
            elif len(n) == 1:
                return False
