from typing import List
def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
    robot.sort()
    factory.sort()

    slots = []
    for pos, limit in factory:
        for _ in range(limit):
            slots.append(pos)

    n = len(robot)
    m = len(slots)
    INF = float('inf')

    dp = [0] * (m + 1)       

    for i in range(n - 1, -1, -1):
        new_dp = [INF] * (m + 1)
        new_dp[m] = INF       
        for j in range(m - 1, -1, -1):
            assign = abs(robot[i] - slots[j]) + dp[j + 1]
            skip   = new_dp[j + 1]
            new_dp[j] = min(assign, skip)
        dp = new_dp

    return dp[0]