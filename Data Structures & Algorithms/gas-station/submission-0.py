class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        current_tank = 0
        total_tank = 0
        start = 0

        for i in range(len(gas)):
            remaining = gas[i] - cost[i]
            current_tank += remaining
            total_tank += remaining

            if current_tank < 0:
                current_tank = 0
                start = i + 1
            
        if total_tank < 0:
            return -1
        return start