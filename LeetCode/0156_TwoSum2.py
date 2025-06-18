class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        init, final = 0, len(numbers)-1
        while init < final:
            if target == numbers[init]+numbers[final]:
                return [init+1, final+1]
            elif target < numbers[init]+numbers[final]:
                final -= 1
            elif target > numbers[init]+numbers[final]:
                init += 1

        return [init+1, final+1]
