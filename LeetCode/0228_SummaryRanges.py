class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []
        if len(nums) == 0:
            return ans
        init = nums[0]
        count = 0
        for i in range(1, len(nums)+1):
            if i == len(nums) or nums[i] != nums[i-1]+1:
                if init == nums[i-1]:
                    ans.append(str(init))
                else:
                    ans.append("{}->{}".format(init, nums[i-1]))

                if i < len(nums):
                    init = nums[i]

        return ans
