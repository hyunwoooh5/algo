class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        for curr_index in range(n):
            curr_gas = 0
            done = True
            for i in range(n):
                curr_gas += gas[(curr_index+i) % n]

                curr_gas -= cost[(curr_index+i) % n]

                if curr_gas < 0:
                    done = False
                    break

            if done:
                return curr_index

        return -1


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        curr_gas = 0
        ans = 0

        for i in range(len(gas)):
            curr_gas += gas[i]-cost[i]

            if curr_gas < 0:
                curr_gas = 0
                ans = i+1

        return ans


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        for i in range(n):
            done = True
            tank = 0
            for j in range(n):
                tank += gas[(i+j) % n]-cost[(i+j) % n]
                if tank < 0:
                    done = False
                    break

            if done:
                return i

        return -1


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                res = i+1

        return res
