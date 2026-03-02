# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while True:
            mid = (left+right)//2
            g = guess(mid)
            if g == 0:
                return mid
            elif g == -1:
                right = mid - 1
            else:
                left = mid+1

        return mid


class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while True:
            m1 = l + (r-l)//3
            m2 = r - (r-l)//3

            if guess(m1) == 0:
                return m1

            if guess(m2) == 0:
                return m2

            if guess(m1) + guess(m2) == 0:
                l = m1+1
                r = m2-1
            elif guess(m1) == -1:
                r = m1 - 1
            else:
                l = m2+1
