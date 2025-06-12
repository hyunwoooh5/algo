class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True

        for i in range(1, num//2+1):
            if i**2 == num:
                return True
            elif i**2 > num:
                return False


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True

        left, right = 1, num
        while left <= right:
            mid = (left+right)//2
            if mid**2 == num:
                return True
            elif mid**2 < num:
                left = mid + 1
            elif mid**2 > num:
                right = mid - 1

        return False
