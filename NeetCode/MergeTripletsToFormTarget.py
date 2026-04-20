class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ans = [0, 0, 0]

        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue

            ans = [max(ans[0], triplet[0]), max(
                ans[1], triplet[1]), max(ans[2], triplet[2])]

        return ans == target


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        curr_x, curr_y, curr_z = 0, 0, 0

        for x, y, z in triplets:
            if x > target[0] or y > target[1] or z > target[2]:
                continue
            else:
                curr_x = max(curr_x, x)
                curr_y = max(curr_y, y)
                curr_z = max(curr_z, z)

        return [curr_x, curr_y, curr_z] == target
