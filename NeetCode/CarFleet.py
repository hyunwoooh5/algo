class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[position[i], speed[i]] for i in range(len(position))]
        cars.sort(key=lambda x: x[0], reverse=True)

        times = [(target-position)/speed for position, speed in cars]

        stack = []

        for time in times:
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
