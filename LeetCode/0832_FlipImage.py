class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(image)
        ans = [i[::-1] for i in image]

        for i in range(n):
            for j in range(n):
                ans[i][j] = 1 - ans[i][j]

        return ans
