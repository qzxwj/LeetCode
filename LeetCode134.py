class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        i = 0
        while i < n:
            j = i
            left = 0
            steps = 0
            while steps < n:
                left += gas[j] - cost[j]
                if left < 0:
                    break
                j = (j + 1) % n
                steps += 1

            if steps == n:
                return i

            i = i + steps + 1

        return -1