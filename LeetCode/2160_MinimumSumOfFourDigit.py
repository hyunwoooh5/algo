class Solution:
    def minimumSum(self, num: int) -> int:
        num = [int(i) for i in str(num)]
        num.sort()
        return 10*(num[0]+num[1]) + (num[2]+num[3])
