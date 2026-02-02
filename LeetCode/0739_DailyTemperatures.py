class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0]*n
        stack = []

        for i, current_temp in enumerate(temperatures):
            while stack and current_temp > temperatures[stack[-1]]:
                prev_day = stack.pop()

                days = i - prev_day

                answer[prev_day] = days

            stack.append(i)

        return answer
