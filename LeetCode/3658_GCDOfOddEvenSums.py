class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumodd = n**2
        sumeven = n*(n+1)

        while sumodd != 0 and sumeven != 0:
            if sumodd > sumeven:
                sumodd -= sumeven
            else:
                sumeven -= sumodd

        return max(sumodd, sumeven)


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n
