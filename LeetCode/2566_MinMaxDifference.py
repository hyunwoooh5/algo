class Solution:
    def minMaxDifference(self, num: int) -> int:
        maximum, minimum = [s for s in str(num)], [s for s in str(num)]

        for i, s in enumerate(maximum):
            if s != '9':
                for j in range(i, len(maximum)):
                    if maximum[j] == s:
                        maximum[j] = '9'
                break

        maximum = int(''.join(maximum))

        s = minimum[0]

        for j in range(len(minimum)):
            if minimum[j] == s:
                minimum[j] = '0'

        minimum = int(''.join(minimum))

        return maximum-minimum
