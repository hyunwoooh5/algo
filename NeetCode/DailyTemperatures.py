class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        stack = []

        for i, curr in enumerate(temperatures):
            while stack and curr > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index

            stack.append(i)

        return ans


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        ans = [0]*n

        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index

            stack.append(i)

        return ans


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        ans = [0]*n

        for i in range(n-2, -1, -1):
            j = i+1  # next day

            while j < n and temperatures[j] <= temperatures[i]:
                if ans[j] == 0:  # no warmer day
                    j = n
                    break

                j += ans[j]

            if j < n:
                ans[i] = j-i

        return ans
