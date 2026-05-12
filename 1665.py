from typing import List
def minimumEffort(self, tasks: List[List[int]]) -> int:
    tasks.sort(key = lambda x: x[0] - x[-1])

    energy = 0
    total_spent = 0

    for actual, minimum in tasks:
        if energy < minimum:
            total_spent += (minimum - energy)
            energy = minimum
        energy -= actual

    return total_spent