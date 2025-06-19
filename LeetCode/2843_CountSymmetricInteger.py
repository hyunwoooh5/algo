class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        ans = 0
        for i in range(low, high+1):
            if len(str(i)) % 2 == 0:
                a1 = str(i)[:len(str(i))//2]
                a2 = str(i)[len(str(i))//2:]
                if sum([int(j) for j in a1]) == sum([int(j) for j in a2]):
                    ans += 1
        return ans
