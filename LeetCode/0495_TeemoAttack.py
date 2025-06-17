class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        ans = duration
        diff = [timeSeries[i+1]-timeSeries[i]
                for i in range(len(timeSeries)-1)]
        for i in range(len(diff)):
            ans += duration
            if diff[i] < duration:
                ans -= duration - diff[i]

        return ans
