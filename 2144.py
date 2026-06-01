from typing import List
def minimumCost(cost: List[int]) -> int:
    n = len(cost)
    cost.sort(reverse=True)

    if n <= 2:
        return sum(cost)
    result = 0

    for i in range(len(cost)):
        position = i + 1
        if position % 3 == 0:
            continue
        result += cost[i]

    return result