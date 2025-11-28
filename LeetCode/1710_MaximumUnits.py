class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        ans = 0
        index = 0
        for i in range(truckSize):
            ans += boxTypes[index][1]
            boxTypes[index][0] -= 1

            if boxTypes[index][0] == 0:
                index += 1

            if index >= len(boxTypes):
                break

        return ans
